from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_code', 'category_name', 'parent_category_id', 'banner_image')
    search_fields = ('category_name',)
    list_filter = ('domestic_corporate',)


admin.site.register(Category, CategoryAdmin)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'group_name')


admin.site.register(Group, GroupAdmin)


class MediaTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'path')


admin.site.register(MediaType, MediaTypeAdmin)


class MediaLibraryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'file_name')
    search_fields = ('related_id', 'file_name')
    list_filter = ('related_type',)


admin.site.register(MediaLibrary, MediaLibraryAdmin)


class MediaSettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')


admin.site.register(MediaSetting, MediaSettingAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand_code', 'brand_name')


admin.site.register(Brand, BrandAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_code', 'product_name', 'category')
    list_filter = ('category', 'mrp', 'sale_price')
    search_fields = ('category__category_name',)


admin.site.register(Product, ProductAdmin)


class GroupProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'groups', 'products')


admin.site.register(GroupProducts, GroupProductsAdmin)


class ProductCategoryAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'attribute_name')


admin.site.register(ProductCategoryAttribute, ProductCategoryAttributeAdmin)


class ProductCategoryAttributeValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute', 'value')


admin.site.register(ProductCategoryAttributeValue, ProductCategoryAttributeValueAdmin)


class ProductAttributesAdmin(admin.ModelAdmin):
    list_display = ('id', 'products', 'attribute', 'attribute_value')


admin.site.register(ProductAttributes, ProductAttributesAdmin)


class ProductCateoryAttributeGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'group_name')


admin.site.register(ProductCateoryAttributeGroup, ProductCateoryAttributeGroupAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_code', 'big_image_url', 'thumb_image_url')


admin.site.register(ProductImage, ProductImageAdmin)


class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('id', 'products', 'name', 'image')
    search_fields = ('name', 'products__product_name', 'slug')


admin.site.register(ProductVariant, ProductVariantAdmin)


class ProductInventoryByVendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'vendor', 'variant',)
    search_fields = ('retail_price', 'sale_price', 'landing_price')


admin.site.register(ProductInventoryByVendor, ProductInventoryByVendorAdmin)


class ProductPriceHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'inventory')
    search_fields = ('inventory__variant__name',)


admin.site.register(ProductPriceHistory, ProductPriceHistoryAdmin)


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'products', 'title', 'review', 'rating')


admin.site.register(ProductReview, ProductReviewAdmin)


class ProductStockHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'inventory', 'last_stock', 'added_stock')


admin.site.register(ProductStockHistory, ProductStockHistoryAdmin)


class ProductVariantImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'variant', 'title', 'image')
    search_fields = ('variant__name',)


admin.site.register(ProductVariantImage, ProductVariantImageAdmin)


class ProductViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'products', 'count')


admin.site.register(ProductView, ProductViewAdmin)


class WarrantyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model')


admin.site.register(Warranty, WarrantyAdmin)


class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'vendor_name', 'page_heading')


admin.site.register(Vendor, VendorAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'parent_id', 'event_date_time')
    list_filter = ('type', 'parent_id')


admin.site.register(Page, PageAdmin)


class BlocksAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'variant', 'page')


admin.site.register(Blocks, BlocksAdmin)


class ExtendedWarrantiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'products', 'category')


admin.site.register(ExtendedWarranties, ExtendedWarrantiesAdmin)


class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'slider_name', 'code', 'width', 'height')


admin.site.register(Slider, SliderAdmin)


class SliderPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'sliders', 'media')


admin.site.register(SliderPhoto, SliderPhotoAdmin)


class SearchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'variant', 'keyword')


admin.site.register(Search, SearchAdmin)


class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'search_term', 'count')


admin.site.register(SearchHistory, SearchHistoryAdmin)


class SettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'type', 'page')
    search_fields = ('code', 'value')


admin.site.register(Settings, SettingsAdmin)


class SpecificationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'variant', 'group')
    search_fields = ('variant__name',)


admin.site.register(Specifications, SpecificationsAdmin)


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(ProductType, ProductTypeAdmin)


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product_type')


admin.site.register(ProductModel, ProductModelAdmin)
