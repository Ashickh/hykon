import random
import json
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.views.generic import TemplateView
from django.db.models import Sum, F
from django.urls import reverse_lazy
import razorpay
from .models import *
from apps.catalogue.models import *
from apps.user.models import Address
from .serializers import *
from apps.user.forms import *

import sys
import traceback


class AddProductToCartView(APIView):
    def post(self, request, *args, **kwargs):
        product_slug = request.data.getlist('product_slug')[0]
        product = ProductVariant.objects.get(slug=product_slug)
        if request.user.is_authenticated:
            if Cart.objects.filter(product=product, user=request.user, placed=False).exists():
                cart_obj = Cart.objects.filter(product=product, user=request.user, placed=False).last()
                cart_obj.quantity += 1
                cart_obj.save()
            else:
                price_obj = ProductPriceHistory.objects.filter(inventory__variant=product).order_by('id').last()
                cart_obj = Cart.objects.create(
                    user=request.user, product=product, quantity=1, price=price_obj.sale_price,
                    retail_price=price_obj.new_retail_price, sale_price=price_obj.new_sale_price)
            response = Response({'status': 'success'})
        else:
            cart_id = request.COOKIES.get('cart_id', [])
            if cart_id:
                cart_id = json.loads(cart_id)
            if Cart.objects.filter(product=product, id__in=cart_id, placed=False).exists():
                cart_obj = Cart.objects.filter(product=product, id__in=cart_id, placed=False).last()
                cart_obj.quantity += 1
                cart_obj.save()
            else:
                price_obj = ProductPriceHistory.objects.filter(inventory__variant=product).order_by('id').last()
                cart_obj = Cart.objects.create(
                    product=product, quantity=1, price=price_obj.sale_price,
                    retail_price=price_obj.new_retail_price, sale_price=price_obj.new_sale_price)
                cart_id.append(cart_obj.id)
            response = Response({'status': 'success'})
            response.set_cookie('cart_id', cart_id)
        return response


class RemoveProductFromCartView(APIView):
    def post(self, request, *args, **kwargs):
        response = Response({'status': 'success'})
        product_slug = request.data.getlist('product_slug')[0]
        whether_delete = request.data.getlist('delete', False)
        product = ProductVariant.objects.get(slug=product_slug)
        cart_id = request.COOKIES.get('cart_id', [])
        if cart_id:
            cart_id = json.loads(cart_id)
        if request.user.is_authenticated:
            if Cart.objects.filter(product=product, user=request.user, placed=False).exists():
                cart_obj = Cart.objects.filter(product=product, user=request.user, placed=False).last()
        else:
            if Cart.objects.filter(product=product, id__in=cart_id, placed=False).exists():
                cart_obj = Cart.objects.filter(
                    product=product, id__in=cart_id, placed=False).last()
        if cart_obj.quantity == 1 or whether_delete:
            if cart_id:
                cart_id.remove(cart_obj.id)
                response.set_cookie('cart_id', cart_id)
            cart_obj.delete()
        else:
            cart_obj.quantity -= 1
            cart_obj.save()
        return response


class CartListView(TemplateView):
    template_name = "order/cart_list.html"

    def get(self, request):
        if request.user.is_authenticated:
            carts = Cart.objects.filter(user=request.user, placed=False)
        else:
            cart_id = request.COOKIES.get('cart_id', [])
            if cart_id:
                cart_id = json.loads(cart_id)
            carts = Cart.objects.filter(id__in=cart_id)
        context = {
            'carts': carts,
            'total_price': carts.aggregate(total=Sum(F('quantity') * F('sale_price')))['total'] if carts else 0,
            'empty_cart_image': MediaLibrary.objects.get(title__iexact='empty cart')
        }
        return render(request, self.template_name, context)


class CheckoutView(TemplateView):
    template_name = "order/checkout.html"
    success_url = reverse_lazy('checkout')

    def get(self, request):

        carts = Cart.objects.filter(user=request.user, placed=False)
        context = {
            'form': AdressForm,
            'carts': carts,
            'total_price': carts.aggregate(total=Sum(F('quantity') * F('sale_price')))['total'],
            'addresses': Address.objects.filter(user=request.user),
            'default_address': Address.objects.filter(user=request.user, is_default=True).last()
        }
        if Order.objects.filter(users=request.user, placed=False).exists():
            order_ids = Order.objects.filter(users=request.user, placed=False).values_list('id', flat=True)
            detail_ids = OrderDetail.objects.filter(orders__id__in=order_ids).values_list('orders__id', flat=True)
            OrderTracking.objects.filter(order_details__id__in=detail_ids).delete()
            OrderDetail.objects.filter(orders__id__in=order_ids).delete()
            Order.objects.filter(users=request.user, placed=False).delete()
        return render(request, self.template_name, context)

    def post(self, request):
        form = AdressForm(request.POST)
        if form.is_valid():
            address_obj = form.save(commit=False)
            address_obj.user = request.user
            if not Address.objects.filter(user=request.user, is_default=True).exists():
                address_obj.is_default = True
            else:
                address_obj.is_default = False
            address_obj.save()
            return redirect(self.success_url)
        else:
            carts = Cart.objects.filter(user=request.user, placed=False)
            context = {
                'form': AdressForm,
                'carts': carts,
                'total_price': carts.aggregate(total=Sum(F('quantity') * F('sale_price')))['total'],
                'addresses': Address.objects.filter(user=request.user)
            }
            return render(request, self.template_name, context)


class CheckoutSummaryView(TemplateView):
    template_name = "order/checkout_detail.html"
    success_url = reverse_lazy('customer-orders')

    def get(self, request):

        carts = Cart.objects.filter(user=request.user, placed=False)
        total_price = carts.aggregate(total=Sum(F('quantity') * F('sale_price')))['total']
        context = {
            'carts': carts,
            'total_price': total_price,
            'address': request.GET.get('address')
        }
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY, settings.RAZORPAY_SECRT))
        print(client)
        amount_main = float(total_price) * float(100)
        order_currency = "INR"
        try:
            response = client.order.create(
                {
                    "amount": amount_main,
                    "currency": order_currency,
                    "receipt": request.user.username,
                    "payment": {
                        "capture": "automatic",
                        "capture_options": {"refund_speed": "normal"},
                    },
                }
            )
        
        except Exception as e:
            print("//////...",e)
    
            err = "\n".join(traceback.format_exception(*sys.exc_info()))
            print(err)
            
            return redirect("checkout")
        
        transaction_id = response["id"]
        address = Address.objects.get(pk=request.GET.get('address'))
        total_mrp = carts.aggregate(total=Sum(F('quantity') * F('retail_price')))['total']
        total_sale_price = carts.aggregate(total=Sum(F('quantity') * F('sale_price')))['total']
        total_discount = total_mrp - total_sale_price
        order_data = {
            'users': request.user, 'transaction_id': transaction_id, 'order_reference_number': transaction_id,
            'total_mrp': total_mrp, 'total_discount': total_discount, 'total_sale_price': total_sale_price,
            'total_final_price': total_sale_price, 'delivery_address_id': address
        }
        order_obj = Order.objects.create(**order_data)
        placed_status = OrderStatusLabelsMaster.objects.get(name__iexact='Placed')
        for cart in carts:
            order = {
                'products': cart.product, 'mrp': cart.price, 'quantity': cart.quantity, 'sale_price': cart.sale_price,
                'price': cart.retail_price, 'discount': cart.retail_price - cart.sale_price, 'status': placed_status,
                'orders': order_obj
            }
            order_detail = OrderDetail.objects.create(**order)
            OrderTracking.objects.create(order_details=order_detail, order_status_labels_master=placed_status,
                                         created_by=request.user, updated_by=request.user)
        context['key'] = settings.RAZORPAY_KEY
        context['order'] = order_obj
        context['logo'] = MediaLibrary.objects.get(title__exact='logo')
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        response = request.POST
        print(response)
        trans_id = response["trans_id"]
        params_dict = {
            "razorpay_payment_id": response["razorpay_payment_id"],
            "razorpay_order_id": response["razorpay_order_id"],
            "razorpay_signature": response["razorpay_signature"],
        }
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY, settings.RAZORPAY_SECRT))
        try:
            pay_status = client.utility.verify_payment_signature(params_dict)
            Order.objects.filter(transaction_id=trans_id).update(status='payment_completed')
            Cart.objects.filter(user=request.user, placed=False).update(placed=True)
        except Exception as e:
            pass
        Order.objects.filter(transaction_id=trans_id).update(placed=True)
        return redirect("customer-orders")


class ReviewProductView(APIView):
    def post(self, request, *args, **kwargs):
        product_obj = ProductVariant.objects.get(pk=request.POST['product_id'])
        ProductReview.objects.update_or_create(user=request.user, products=product_obj, defaults={
            'user': request.user, 'products': product_obj, 'title': request.POST['title'],
            'review': request.POST['review'], 'rating': float(request.POST['rating'])
        })
        return Response()

