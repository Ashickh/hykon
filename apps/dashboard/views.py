from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView
)
from apps.catalogue.models import Category, ProductVariant, Page, Settings,  Warranty, Product, Enquiry
from apps.order.models import OrderDetail, OrderTracking
from apps.order.models import Order
from apps.cms.models import BannerPhoto
from apps.catalogue.forms import WarrantyForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.views.generic import View, DetailView
from django.core.paginator import Paginator



class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'



class ProductListView(TemplateView):
    template_name = "dashboard/products.html"
    def get(self,request):
        products = ProductVariant.objects.all()
        # print(prod)
            # Number of items to display per page
        items_per_page = 10

        # Create a Paginator object
        paginator = Paginator(products, items_per_page)

        # Get the current page number from the request's GET parameters
        page_number = request.GET.get('products')

        # Get the corresponding page from the Paginator
        page = paginator.get_page(page_number)
        context = {
            'products': products,
            'page':page
        }
        return render(request,self.template_name,context)

class OrderDashboardView(View):

    def get(self,request):
        orders = Order.objects.all()
        # print(orders)
        return render(request,"dashboard/orders.html",{'orders':orders})


class EnquiryDashboardView(View):

    def get(self,request):
        enquiry = Enquiry.objects.all()
        # print(orders)
        return render(request,"dashboard/enquiry.html",{'enquiry':enquiry})
    
class WarrantyListDashboardView(View):

    def get(self,request):
        warranty_list = Warranty.objects.all()
        # print(orders)
        return render(request,"dashboard/warranty_reg_list.html",{'warranty_list':warranty_list})

class AdminProfileView(TemplateView):
    template_name = 'dashboard/profile.html'


    
class OrderDetailView(DetailView):
    model = OrderDetail
    template_name = "dashboard/order_detail.html"

    context_object_name = 'parent_order'

    pk_url_kwarg = 'id'

class OrderTrackView(DetailView):
    model = OrderTracking

    template_name = "dashboard/order_track.html"

    context_object_name = 'track_order'

    pk_url_kwarg = 'id'
