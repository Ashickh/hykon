import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, ListView
)
from requests import Response
from rest_framework import status

from apps.catalogue.models import Category, ProductVariant, Page, Settings, MediaLibrary, Enquiry, Product
from apps.home.forms import EnquiryForm
from apps.order.models import Order
from apps.cms.models import BannerPhoto
from apps.catalogue.forms import WarrantyForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.views.generic import View
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response



class HomeView(TemplateView):
    template_name = "home/home.html"

    def get(self, request):
        request.session['logged_in'] = True if request.user.is_authenticated else False
        print(request.session)
        hl_items = ['hl-title', 'hl-description', 'hl-s1-title', 'hl-s1-icon', 'hl-s1-summary',
                    'hl-s2-title', 'hl-s2-icon', 'hl-s2-summary',
                    'hl-s3-title', 'hl-s3-icon', 'hl-s3-summary',
                    'hl-s4-title', 'hl-s4-icon', 'hl-s4-summary',
                    'start-up', 'employees', 'companies', 'crore-turnover',
                    'cmd-image', 'cmd-message-description', 'cmd-message-title']
        hl_values = Settings.objects.filter(code__in=hl_items)
        hl_values_dict = {}
        for hl in hl_values:
            hl_values_dict[hl.code.replace('-', '_')] = hl
        context = {
            'Blogs': Page.objects.filter(type='Blog').order_by('-created_at'),
            'hl_values': hl_values_dict,
            'awards': BannerPhoto.objects.filter(banners__code='awards').order_by('created_at')
        }
        request.session
        return render(request, self.template_name, context)


class CategoryView(TemplateView):
    template_name = "home/category.html"

    def get(self, request, slug):
        main_category = Category.objects.get(slug=slug)
        sub_categories = Category.objects.filter(parent_category_id=main_category)
        count = len(sub_categories)
        if count % 2 == 0:
            mid = int(count / 2)
        else:
            mid = int(count / 2) + 1
        first_list = sub_categories[0:mid]
        second_list = sub_categories[mid:count]
        banner_photos = BannerPhoto.objects.filter(banners__banner_name=main_category.category_name)
        context = {
            'request_obj': request,
            'main_category': main_category,
            'sub_categories': sub_categories,
            'category_id': slug,
            'first_list': first_list,
            'second_list': second_list,
            'banners': banner_photos
        }
        return render(request, self.template_name, context)


class ProductListView(TemplateView):
    template_name = "home/product_list.html"

    def get(self, request, slug):
        main_category = Category.objects.get(slug=slug).parent_category_id
        sub_categories = Category.objects.filter(parent_category_id=main_category)
        context = {
            'request_obj': request,
            'main_category': main_category,
            'sub_categories': sub_categories,
            'category_id': slug,
            'selected_category': Category.objects.get(slug=slug)
        }
        return render(request, self.template_name, context)


class ProductDetailView(TemplateView):
    template_name = "home/product_detail.html"

    def get(self, request, slug):
        product_variant = ProductVariant.objects.get(slug=slug)
        main_category = Category.objects.get(slug=product_variant.products.category.parent_category_id.slug)
        variant_products = ProductVariant.objects.filter(products=product_variant.products)
        print(variant_products)
        context = {
            'product_variant': product_variant,
            'main_category': main_category,
            'variant_products': variant_products
        }
        return render(request, self.template_name, context)


class NewsEventsView(TemplateView):
    template_name = "home/news_events.html"

    def get(self, request):
        context = {
            'newses': Page.objects.filter(type='News'),
            'events': Page.objects.filter(type='Events').order_by('-event_date_time')
        }
        return render(request, self.template_name, context)


class NewsDetailView(TemplateView):
    template_name = "home/news_detail.html"

    def get(self, request, slug):
        news = Page.objects.get(slug=slug)
        news.views += 1
        news.save()
        context = {
            'news': news,
            'more_news': Page.objects.filter(type='News').exclude(slug=slug)
        }
        return render(request, self.template_name, context)


class EventDetailView(TemplateView):
    template_name = "home/event_detail.html"

    def get(self, request, slug):
        event = Page.objects.get(slug=slug)
        event.views += 1
        event.save()
        context = {
            'event': event,
            'more_events': Page.objects.filter(type='Events').exclude(slug=slug)
        }
        return render(request, self.template_name, context)


class BlogsView(TemplateView):
    template_name = "home/blogs.html"

    def get(self, request):
        if request.GET.get('sort', False) == 'views':
            blogs = Page.objects.filter(type='Blog').order_by('-views')
        else:
            blogs = Page.objects.filter(type='Blog').order_by('-created_at')
        context = {
            'blogs': blogs
        }
        return render(request, self.template_name, context)


class BlogDetailView(TemplateView):
    template_name = "home/blog_detail.html"

    def get(self, request, slug):
        blog = Page.objects.get(slug=slug)
        blog.views += 1
        blog.save()
        context = {
            'current_blog': blog,
            'more_blogs': Page.objects.filter(type='Blog').order_by('-created_at').exclude(slug=slug)
        }
        return render(request, self.template_name, context)


class AboutView(TemplateView):
    template_name = "home/about.html"

    def get(self, request):
        context = {
            'about_intro_image': Settings.objects.get(code='about_intro_image'),
            'about_mission_image': Settings.objects.get(code='about_mission_image'),
            'about_vision_image': Settings.objects.get(code='about_vision_image'),
            'about_mission_desc': Settings.objects.get(code='about_mission_desc'),
            'about_mission_title': Settings.objects.get(code='about_mission_title'),
            'about_highlights': Settings.objects.get(code='about_highlights'),
            'about_vision_desc': Settings.objects.get(code='about_vision_desc'),
            'about_vision_title': Settings.objects.get(code='about_vision_title'),
            'about_description': Settings.objects.get(code='about_description'),
            'about_title': Settings.objects.get(code='about_title'),
            'why_hykon': Settings.objects.get(code='why_hykon'),
            'about_banner_image': Settings.objects.get(code='about_banner_image'),
        }
        return render(request, self.template_name, context)


class WarrantyView(TemplateView):
    template_name = 'home/warranty_registration.html'
    success_url = reverse_lazy('warranty')

    def get(self, request):
        context = {
            'warranty_image': MediaLibrary.objects.get(title__iexact='warranty'),
            'form': WarrantyForm,
            'billing_adresses': ['billing_address1', 'billing_address2', 'billing_landmark', 'billing_state',
                                 'billing_district', 'billing_pincode'],
            'installation_addresses': ['installation_address1', 'installation_address2',
                                       'installation_landmark', 'installation_state', 'installation_district',
                                       'installation_pincode']
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = WarrantyForm(request.POST)
        if form.is_valid():
            mail = form.cleaned_data.get("mail")
            name = form.cleaned_data.get("name")
            # product_type = form.cleaned_data.get("product_type")
            # model = form.cleaned_data.get("model")
            invoice_number = form.cleaned_data.get("invoice_number")
            serial_number = form.cleaned_data.get("serial_number")

            message = 'Hi' f"{name} ...! \n\n Invoive Number: {invoice_number} \n\n Serial Number: {serial_number} \n \n This product is covered by a limited warranty for a period of one year from the date of purchase. \n \n For warranty claims, please contact our customer service department..!"

            # html_content = """ <!DOCTYPE html>
            #                     <html>
            #                     <head>
            #                         <title>Hykon Warranty Card</title>
            #                     </head>
            #                     <body>
            #                         <h3>Warranty Card</h3>
            #                         <h3> Hi. """+(name)+"""</h3>
            #                         <table>
            #                         <tr>
            #                         <th>PRODUCT TYPE</th>
            #                         <th>MODEL</th>
            #                         <th>INVOICE NUMBER</th>
            #                         <th>SERIAL NUMBER</th>
            #                         </tr>
            #                         <tr>
                                    
                                    
            #                         <td>"""+(invoice_number)+"""</td>
            #                         <td>"""+(serial_number)+"""</td>
            #                         </tr>
            #                         </table>
            #                         <p>This product is covered by a limited warranty for a period of one year from the date of purchase.</p>
            #                         <ul>
            #                             <li>Warranty applies only to the original purchaser of the product.</li>
            #                             <li>Warranty covers defects in material and workmanship only.</li>
            #                             <li>Warranty does not cover damage caused by misuse, abuse, or improper handling.</li>
            #                             <li>For warranty claims, please contact our customer service department.</li>
            #                         </ul>
            #                     </body>
            #                     </html>
            #                     """
            form.save()
         
            send_mail(
                    subject = 'Hykon Product Warranty',
                    message = message,
                    from_email = settings.EMAIL_HOST_USER,
                    recipient_list = [mail],
                    fail_silently = False,
                    ) 
            return redirect(self.success_url)
        else:
            context = {
                'warranty_image': MediaLibrary.objects.get(title__iexact='warranty'),
                'form': form,
                'billing_adresses': ['billing_address1', 'billing_address2', 'billing_landmark', 'billing_state',
                                     'billing_district', 'billing_pincode'],
                'installation_addresses': ['installation_address1', 'installation_address2',
                                           'installation_landmark', 'installation_state', 'installation_district',
                                           'installation_pincode']
            }
            return render(request, self.template_name, context)

@csrf_exempt
def EnquiryView(request):
    if request.method != "POST":
        return JsonResponse({"message": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)
    form = EnquiryForm(request.POST)
    if form.is_valid():
        
        form.save()
        
        form.instance.send_email_notifications()
        return JsonResponse({"message": "Success"})

    return JsonResponse({"message": "Please check all the fields", 'errors': form.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class DeliveryPolicyView(TemplateView):
    template_name = 'home/delivery_policy.html'


class CareerView(TemplateView):
    template_name = 'home/career.html'


class CareerApplicationView(TemplateView):
    template_name = 'home/applicationform.html'



class SearchView(TemplateView):
   template_name = 'home/search_results.html'

   def get(self, request):
        query = request.GET.get('query', '')
        print(query)
        product_variant = Product.objects.filter(product_name__icontains=query)
        print(product_variant)
        product_list = ProductVariant.objects.filter(name__icontains=query)
       
        context = {
                'query': query,
                'product_list': product_list,
                'product_variant': product_variant
              
        }     
   
        return render(request, self.template_name, context)


class FilterProductView(TemplateView):
    template_name = "home/product_list.html"

    def get(self, request, slug):
        # print(request.GET)
        selected_categories = request.GET.getlist('category')
        # convert the categories as alist
        new_string = str(selected_categories).replace("'", "")
        cleaned_string = str(new_string).strip('[]')  
        category_list = cleaned_string.split(',')
        print(category_list)

        main_category = Category.objects.get(slug=slug).parent_category_id
        sub_categories = Category.objects.filter(parent_category_id=main_category)
        filtered_category = Category.objects.filter(slug__in=category_list)
        print(filtered_category)
        
        context = {
            'request_obj': request,
            'main_category': main_category,
            'sub_categories': sub_categories,
            'category_id': slug,
            'filtered_category': filtered_category
            
        }
        return render(request, self.template_name, context)
