import os
from django import template
import requests
from django.core.files.storage import default_storage
from apps.catalogue.models import Product, ProductVariant, ProductPriceHistory, ProductVariantImage, Specifications, \
    ProductReview, MediaLibrary
from apps.order.models import OrderDetail, OrderTracking

register = template.Library()


# {% if category.brochure_pdf.file_path|file_exists:request_obj %}
@register.filter
def file_exists(file_path, request):
    """
    Checks if a file exists in the given file path
    """
    url = default_storage.url(file_path)
    if url.startswith('/'):
        url = 'http://' + request.get_host() + url
    response = requests.get(url)
    return True if response.status_code == 200 else False


@register.filter
def product_of_category(category_obj):
    
    return Product.objects.filter(category=category_obj)[0]


@register.filter
def variants_of_product(product_obj):
    return ProductVariant.objects.filter(products=product_obj)


@register.filter
def get_price_of_product(product_variant_obj):
    return ProductPriceHistory.objects.filter(inventory__variant=product_variant_obj).order_by('id').last()


@register.filter
def product_variant_image(product_variant_obj):
    if ProductVariantImage.objects.filter(variant=product_variant_obj).exists():
        return ProductVariantImage.objects.filter(variant=product_variant_obj)[0].get_image_path
    else:
        return ''


@register.filter
def specifications_of_product(product_variant_obj):
    spec_groups = list(set(Specifications.objects.filter(
        variant=product_variant_obj).values_list('group', flat=True)))
    specifications = []
    for group in spec_groups:
        specifications.append({
            'group': group,
            'specs': Specifications.objects.filter(variant=product_variant_obj, group=group)})
    return specifications


@register.filter
def get_product_reviews(product_obj):
    return ProductReview.objects.filter(products=product_obj).order_by('-id')


@register.filter
def get_variant_images(product_variant_obj):
    images = ProductVariantImage.objects.filter(variant=product_variant_obj)
    return images


@register.filter
def get_product(cart_obj):
    return cart_obj.sale_price * cart_obj.quantity

@register.filter
def get_sub_orders(order_obj):
    return OrderDetail.objects.filter(orders=order_obj)


@register.filter
def get_order_tracking(order_obj):
    return OrderTracking.objects.filter(order_details__orders=order_obj)
