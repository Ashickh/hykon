from django.contrib import admin
from .models import *


class WishlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'variant')


admin.site.register(Wishlist, WishlistAdmin)


class OfferCategoryAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(OfferCategory, OfferCategoryAdmin)


class OfferComboFreeProductAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(OfferComboFreeProduct, OfferComboFreeProductAdmin)


class OfferComboProductAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(OfferComboProduct, OfferComboProductAdmin)


class OfferGroupAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(OfferGroup, OfferGroupAdmin)


class OfferPriceProductAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(OfferPriceProduct, OfferPriceProductAdmin)


class OfferAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(Offer, OfferAdmin)


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'orders', 'products', 'quantity', 'mrp', 'sale_price', 'price', 'status')
    list_filter = ('status',)
    search_fields = ('orders__id',)


admin.site.register(OrderDetail, OrderDetailAdmin)


class OrderStatusLabelsMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'display_order', 'type')


admin.site.register(OrderStatusLabelsMaster, OrderStatusLabelsMasterAdmin)


class OrderTrackingAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_details', 'order_status_labels_master')
    list_filter = ('order_status_labels_master',)
    search_fields = ('order_details__id',)


admin.site.register(OrderTracking, OrderTrackingAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'users', 'placed', 'status', 'transaction_id', 'order_reference_number', 'payment_method',
                    'payment_status', 'payment_receive_status')
    list_filter = ('payment_method', 'payment_status', 'payment_receive_status', 'status')


admin.site.register(Order, OrderAdmin)


class CouponAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(Coupon, CouponAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'retail_price', 'sale_price', 'placed')


admin.site.register(Cart, CartAdmin)


class CancelOrderReasonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display_order')


admin.site.register(CancelOrderReason, CancelOrderReasonAdmin)
