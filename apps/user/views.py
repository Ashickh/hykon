import json
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout as auth_logout
from django.urls import reverse
from django.contrib.auth.hashers import check_password
from .serializers import *
from .models import CityPincode, User, Address
from apps.catalogue.models import ProductModel
from .forms import *
from apps.order.models import Order, CancelOrderReason, OrderDetail, OrderStatusLabelsMaster, OrderTracking, Cart


class GetPincodeDetails(ListAPIView):
    serializer_class = PincodeSerializer
    queryset = CityPincode.objects.all()

    def get(self, request, *args, **kwargs):
        if request.GET.get('pincode_id', False) == '':
            return Response([])
        queryset = self.get_queryset().filter(pk=request.GET['pincode_id'])
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class GetProductTypeModelsView(ListAPIView):
    serializer_class = ProductModelSerializer
    queryset = ProductModel.objects.all()

    def get(self, request, *args, **kwargs):
        if request.GET.get('product_type', False) == '':
            return Response([])
        queryset = self.get_queryset().filter(product_type__pk=request.GET['product_type'])
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


@method_decorator(csrf_exempt, name='dispatch')
class CustomerRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        user_data = dict(request.POST)
        user_obj = User.objects.create_user(
            username=user_data['email'][0], first_name=user_data['first_name'][0], last_name=user_data['last_name'][0],
            email=user_data['email'][0], password=user_data['password'][0], password_resets=True)
        user_obj.save()
        return Response()


@method_decorator(csrf_exempt, name='dispatch')
class CustomerLoginView(APIView):
    def post(self, request, *args, **kwargs):
        user_data = dict(request.POST)
        username = user_data['username'][0]
        password = user_data['password'][0]
        print(username)
        user = authenticate(request, username=username, password=password)
        print (request.session.session_key)
        if user is not None:
            login(request, user)
            cart_id = request.COOKIES.get('cart_id', [])
            response = Response({'status': 'success'})
            if cart_id:
                cart_id = json.loads(cart_id)
                response.set_cookie('cart_id', [])
                if Cart.objects.filter(id__in=cart_id, placed=False).exists():
                    for cart in cart_id:
                        cart_obj = Cart.objects.get(placed=False, id=cart)
                        if Cart.objects.filter(placed=False, product=cart_obj.product, user=user).exists():
                            exist_cart = Cart.objects.filter(placed=False, product=cart_obj.product, user=user).last()
                            exist_cart.quantity += cart_obj.quantity
                            exist_cart.save()
                            cart_obj.delete()
                        else:
                            cart_obj.user = user
                            cart_obj.save()
            return response
        else:
            return Response({'status': 'failed', 'message': 'Invalid username or password.'})


class CustomerLogoutView(LogoutView):
    # Redirect to home page after logout
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        """Logout may be done via POST."""
        auth_logout(request)
        return redirect(self.success_url)


class CustomerDashboardView(TemplateView):
    template_name = "customer/dashboard.html"
    success_url = reverse_lazy('customer-dashboard')

    def get(self, request):
        default_address = Address.objects.filter(user=request.user, is_default=True).last()
        context = {
            'user': request.user,
            'form': AdressForm,
            'default_address': default_address
        }
        if default_address:
            context['edit_form'] = AdressForm(instance=default_address)
        return render(request, self.template_name, context)

    def post(self, request):
        default_address = Address.objects.filter(user=request.user, is_default=True).last()
        if default_address:
            form = AdressForm(self.request.POST, instance=default_address)
            if form.is_valid():
                form.save()
                return redirect(self.success_url)
        else:
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
        context = {
            'user': request.user,
            'form': AdressForm,
            'default_address': Address.objects.filter(user=request.user, is_default=True).last()
        }
        return render(request, self.template_name, context)


class CustomerProfileView(TemplateView):
    template_name = "customer/profile.html"
    success_url = reverse_lazy('customer-profile')

    def get(self, request):
        context = {
            'form': UserForm(instance=request.user)
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserForm(self.request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        context = {
            'form': UserForm(instance=request.user)
        }
        return render(request, self.template_name, context)


class CustomerOrdersView(TemplateView):
    template_name = "customer/orders.html"

    def get(self, request):
        context = {
            'orders': Order.objects.filter(users=request.user, placed=True).order_by('-created_at')
        }
        return render(request, self.template_name, context)


class CustomerAddressView(TemplateView):
    template_name = "customer/address.html"
    success_url = reverse_lazy('customer-address')

    def get(self, request):
        address_objs = Address.objects.filter(user=request.user)
        addresses = []
        for address in address_objs:
            addresses.append({
                'address_obj': address,
                'form': AdressForm(instance=address)
            })
        context = {
            'addresses': addresses,
            'form': AdressForm
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = AdressForm(request.POST)
        if form.is_valid():
            if 'id' in request.POST:
                instance = Address.objects.get(id=request.POST['id'])
                form = AdressForm(request.POST, instance=instance)
                form.save()
            else:
                address_obj = form.save(commit=False)
                address_obj.user = request.user
                if not Address.objects.filter(user=request.user, is_default=True).exists():
                    address_obj.is_default = True
                else:
                    address_obj.is_default = False
                address_obj.save()
            return redirect(self.success_url)
        address_objs = Address.objects.filter(user=request.user)
        addresses = []
        for address in address_objs:
            addresses.append({
                'address_obj': address,
                'form': AdressForm(instance=address)
            })
        context = {
            'addresses': addresses,
            'form': AdressForm
        }
        return render(request, self.template_name, context)


class CustomerOrderTrackView(TemplateView):
    template_name = "customer/track_order.html"
    success_url = reverse_lazy('customer-order-track')

    def get(self, request, order_id):
        context = {
            'order': Order.objects.get(pk=order_id),
            'cancelled': ['Cancelled', 'Requested for Cancel'],
            'cancel_reasons': CancelOrderReason.objects.all().order_by('display_order')
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        url = reverse('customer-order-track', kwargs={"order_id": kwargs['order_id']})
        cancel_request = OrderStatusLabelsMaster.objects.get(name__iexact='Requested for Cancel')
        OrderDetail.objects.filter(
            pk=request.POST['sub_order']).update(
            cancelled_reason=request.POST['cancelled_reason'], other_reason=request.POST['other_reason'],
            status=cancel_request)
        Order.objects.filter(pk=kwargs['order_id']).update(cancelled_reason=request.POST['cancelled_reason'],
                                                           other_reason=request.POST['other_reason'])
        OrderTracking.objects.filter(order_details__id=request.POST['sub_order']
                                     ).update(order_status_labels_master=cancel_request)
        return redirect(url)


class CustomerChangePasswordView(APIView):

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user.username)
        current_password = request.POST['old']
        new_password = request.POST['new']
        if check_password(current_password, user.password):
            user.set_password(new_password)
            user.save()
            response = {
                'status': 'success',
                'message': 'Password changed successfully'
            }
        else:
            response = {
                'status': 'failed',
                'message': 'Current password entered is not correct'
            }
        return Response(response)



