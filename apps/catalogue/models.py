from django.core.mail import send_mail
from django.db import models
import os
from django.db.models import Avg
from django.conf import settings


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_code = models.CharField(max_length=250, blank=True, null=True)
    # parent_category_id = models.IntegerField(blank=True, null=True)
    parent_category_id = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    category_name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    priority = models.IntegerField()
    type = models.CharField(max_length=100, blank=True, null=True)
    policies = models.TextField(blank=True, null=True)
    top_description = models.TextField(blank=True, null=True)
    bottom_description = models.TextField(blank=True, null=True)
    page_title = models.TextField(blank=True, null=True)
    browser_title = models.CharField(max_length=500, blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    tagline = models.TextField(blank=True, null=True)
    banner_image = models.ForeignKey(
        'MediaLibrary', blank=True, null=True, on_delete=models.SET_NULL, related_name='banner_image')
    thumbnail_image = models.ForeignKey(
        'MediaLibrary', blank=True, null=True, on_delete=models.SET_NULL, related_name='thumbnail_image')
    brochure_pdf = models.ForeignKey(
        'MediaLibrary', blank=True, null=True, on_delete=models.SET_NULL, related_name='brochure_pdf')
    is_popular = models.IntegerField()
    domestic_corporate = models.IntegerField(choices=[
        (0, 'None'),
        (1, 'Domestic'),
        (2, 'Corporate')
    ], default=0)
    # is_domestic = models.IntegerField()
    # is_corporate = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'categories'

    def get_banner_image_path(self):
        if self.banner_image_id and self.banner_image.file_path:
            return self.banner_image.file_path.url

    def get_thumbnail_image_path(self):
        if self.thumbnail_image_id and self.thumbnail_image.file_path:
            return self.thumbnail_image.file_path.url

    def get_brochure_pdf_path(self):
        if self.brochure_pdf_id and self.brochure_pdf.file_path:
            return self.brochure_pdf.file_path.url

    def __str__(self):
        return self.category_name


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=250)
    status = models.IntegerField()
    created_by = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True, blank=True,
                                   db_column='created_by', related_name='created_by')
    updated_by = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True, blank=True,
                                   db_column='updated_by', related_name='updated_by')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'groups'

    def __str__(self):
        return self.group_name


class MediaType(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)
    path = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'media_types'

    def __str__(self):
        return self.type


class MediaLibrary(models.Model):
    id = models.AutoField(primary_key=True)
    file_name = models.TextField()
    file_path = models.FileField(max_length=250)
    thumb_file_path = models.FileField(max_length=250)
    file_type = models.CharField(max_length=100)
    file_size = models.CharField(max_length=100)
    dimensions = models.CharField(max_length=50, blank=True, null=True)
    media_type = models.CharField(max_length=120)
    title = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    alt_text = models.CharField(max_length=250, blank=True, null=True)
    related_type = models.CharField(max_length=20, blank=True, null=True)
    related_id = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey('user.User', on_delete=models.SET_NULL,
                                   db_column='created_by', blank=True, null=True, related_name='media_created_by')
    updated_by = models.ForeignKey('user.User', on_delete=models.SET_NULL,
                                   db_column='updated_by', blank=True, null=True, related_name='media_updated_by')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    media_type_0 = models.ForeignKey('MediaType', on_delete=models.SET_NULL,
                                     db_column='media_type_id', blank=True,
                                     null=True)  # Field renamed because of name conflict.

    class Meta:
        managed = True
        db_table = 'media_library'

    def __str__(self):
        return self.file_name

    def get_file_path(self):
        if self.file_path:
            return self.file_path.url

    def get_thumb_file_path(self):
        if self.thumb_file_path:
            return self.thumb_file_path.url


class MediaSetting(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey('MediaType', on_delete=models.SET_NULL, blank=True, null=True)
    width = models.IntegerField()
    height = models.IntegerField()
    created_by = models.ForeignKey('user.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   db_column='created_by', related_name='media_setting_created_by')
    updated_by = models.ForeignKey('user.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   db_column='updated_by', related_name='media_setting_updated_by')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'media_settings'

    def __str__(self):
        return self.type.type


class Brand(models.Model):
    id = models.BigAutoField(primary_key=True)
    brand_code = models.CharField(max_length=250, blank=True, null=True)
    brand_name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    website = models.CharField(max_length=250, blank=True, null=True)
    media = models.ForeignKey('MediaLibrary', on_delete=models.SET_NULL, blank=True, null=True)
    page_heading = models.CharField(max_length=250, blank=True, null=True)
    browser_title = models.CharField(max_length=250, blank=True, null=True)
    meta_description = models.CharField(max_length=250, blank=True, null=True)
    meta_keywords = models.CharField(max_length=520, blank=True, null=True)
    status = models.IntegerField()
    created_by = models.ForeignKey('user.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   db_column='created_by', related_name='brand_created_by')
    updated_by = models.ForeignKey('user.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   db_column='updated_by', related_name='brand_updated_by')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'brands'

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_code = models.CharField(max_length=250, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    product_name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    use_psp = models.IntegerField()
    tagline = models.CharField(max_length=250, blank=True, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, blank=True, null=True)
    vendor = models.ForeignKey('Vendor', on_delete=models.SET_NULL, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    top_description = models.TextField(blank=True, null=True)
    bottom_description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    mrp = models.FloatField(blank=True, null=True)
    sale_price = models.FloatField(blank=True, null=True)
    hsn_code = models.IntegerField(blank=True, null=True)
    cgst = models.IntegerField(blank=True, null=True)
    sgst = models.IntegerField(blank=True, null=True)
    igst = models.IntegerField(blank=True, null=True)
    is_featured_in_home_page = models.IntegerField()
    is_featured_in_category = models.IntegerField()
    is_new = models.IntegerField()
    is_top_seller = models.IntegerField()
    is_today_deal = models.IntegerField()
    is_active = models.IntegerField()
    is_completed = models.IntegerField()
    default_image_id = models.IntegerField(blank=True, null=True)
    page_heading = models.CharField(max_length=250)
    browser_title = models.CharField(max_length=250, blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    is_warranty_product = models.IntegerField()
    created_by = models.ForeignKey(
        'user.User', on_delete=models.SET_NULL, db_column='created_by', blank=True, null=True,
        related_name='product_created_by')
    updated_by = models.ForeignKey(
        'user.User', on_delete=models.SET_NULL, db_column='updated_by', blank=True, null=True,
        related_name='product_updated_by')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'products'

    def __str__(self):
        return self.product_name

    def get_product_rating(self):
        average = ProductReview.objects.filter(
            pk=self.pk).aggregate(Avg('rating'))['rating__avg']
        return int(average) if average else 0


class GroupProducts(models.Model):
    id = models.AutoField(primary_key=True)
    groups = models.ForeignKey('Group', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    products = models.ForeignKey('Product', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'group_products'

    def __str__(self):
        return self.groups.group_name


class ProductCategoryAttribute(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    attribute_name = models.CharField(max_length=191)
    attribute_type = models.CharField(max_length=20)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)
    show_as_variant = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_cateory_attributes'

    def __str__(self):
        return self.attribute_name


class ProductCategoryAttributeValue(models.Model):
    id = models.AutoField(primary_key=True)
    attribute = models.ForeignKey('ProductCategoryAttribute', on_delete=models.SET_NULL, blank=True, null=True)
    value = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_cateory_attribute_values'

    def __str__(self):
        return self.attribute.attribute_name


class ProductAttributes(models.Model):
    id = models.AutoField(primary_key=True)
    products = models.ForeignKey('Product', on_delete=models.SET_NULL, blank=True, null=True)
    attribute = models.ForeignKey('ProductCategoryAttribute', on_delete=models.SET_NULL, blank=True, null=True)
    attribute_value = models.ForeignKey(
        'ProductCategoryAttributeValue', on_delete=models.SET_NULL, blank=True, null=True)
    attribute_value_0 = models.CharField(db_column='attribute_value', max_length=250, blank=True,
                                         null=True)  # Field renamed because of name conflict.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_attributes'

    def __str__(self):
        return self.products.product_name


class ProductCateoryAttributeGroup(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    group_name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_cateory_attribute_groups'

    def __str__(self):
        return self.group_name


class ProductImage(models.Model):
    id = models.AutoField(primary_key=True)
    product_code = models.CharField(max_length=250, blank=True, null=True)
    is_main = models.IntegerField()
    big_image_url = models.FileField(max_length=500, blank=True, null=True)
    thumb_image_url = models.FileField(max_length=500, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'product_images_tb'

    def __str__(self):
        return self.product_code


class ProductVariant(models.Model):
    id = models.AutoField(primary_key=True)
    search = models.CharField(max_length=250, blank=True, null=True)
    products = models.ForeignKey('Product', on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    code = models.CharField(max_length=250, blank=True, null=True)
    level1_attribute_value_id = models.IntegerField(blank=True, null=True)
    level2_attribute_value_id = models.IntegerField(blank=True, null=True)
    level3_attribute_value_id = models.IntegerField(blank=True, null=True)
    is_default = models.IntegerField()
    sku = models.CharField(max_length=50, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    image = models.ForeignKey('MediaLibrary', on_delete=models.SET_NULL, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    reviews = models.IntegerField(blank=True, null=True)
    offer_status = models.IntegerField()
    combo_offer_status = models.IntegerField()
    is_new = models.IntegerField()
    is_topseller = models.IntegerField()
    is_active = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(
        'user.User', on_delete=models.SET_NULL, db_column='created_by', blank=True, null=True,
        related_name='product_variants_created_by')
    updated_by = models.ForeignKey(
        'user.User', on_delete=models.SET_NULL, db_column='updated_by', blank=True, null=True,
        related_name='product_variants_updated_by')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_variants'

    def __str__(self):
        return self.name

    def get_image_path(self):
        if self.image_id and self.image.file_path:
            return self.image.file_path.url


class ProductInventoryByVendor(models.Model):
    id = models.AutoField(primary_key=True)
    vendor = models.ForeignKey('Vendor', on_delete=models.SET_NULL, blank=True, null=True)
    variant = models.ForeignKey('ProductVariant', on_delete=models.SET_NULL, blank=True, null=True)
    barcode = models.CharField(max_length=250, blank=True, null=True)
    retail_price = models.FloatField(blank=True, null=True)
    sale_price = models.FloatField(blank=True, null=True)
    landing_price = models.FloatField(blank=True, null=True)
    available_quantity = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'product_inventory_by_vendor'

    def __str__(self):
        return str(self.id)


class ProductPriceHistory(models.Model):
    id = models.AutoField(primary_key=True)
    inventory = models.ForeignKey(ProductInventoryByVendor, on_delete=models.SET_NULL, blank=True, null=True)
    retail_price = models.FloatField(blank=True, null=True)
    sale_price = models.FloatField(blank=True, null=True)
    new_retail_price = models.FloatField(blank=True, null=True)
    new_sale_price = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'product_price_history'

    def __str__(self):
        return str(self.id)

    def get_discount_percentage(self):
        try:
            return int(((self.sale_price - self.new_sale_price) / self.new_sale_price) * 100)
        except:
            return 0


class ProductReview(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('user.User', on_delete=models.SET_NULL, blank=True, null=True)
    products = models.ForeignKey('ProductVariant', on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=250)
    review = models.TextField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = True
        db_table = 'product_reviews'

    def __str__(self):
        return self.title


class ProductStockHistory(models.Model):
    id = models.AutoField(primary_key=True)
    inventory = models.ForeignKey('ProductInventoryByVendor', on_delete=models.SET_NULL, blank=True, null=True)
    last_stock = models.IntegerField(blank=True, null=True)
    added_stock = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'product_stock_history'

    def __str__(self):
        return self.inventory.barcode


class ProductVariantImage(models.Model):
    id = models.AutoField(primary_key=True)
    variant = models.ForeignKey('ProductVariant', on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ForeignKey('MediaLibrary', on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    alt = models.CharField(max_length=250, blank=True, null=True)
    is_common = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_variant_images'

    def __str__(self):
        return self.title

    def get_image_path(self):
        if self.image_id and self.image.big_image_url:
            return self.image.big_image_url.url

    def get_thumb_image_path(self):
        if self.image_id and self.image.thumb_image_url:
            return self.image.thumb_image_url.url


class ProductView(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('user.User', on_delete=models.SET_NULL, blank=True, null=True)
    products = models.ForeignKey('Product', on_delete=models.SET_NULL, blank=True, null=True)
    count = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'product_views'

    def __str__(self):
        return self.products.product_name


class ProductType(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'product_type'


class ProductModel(models.Model):
    name = models.CharField(max_length=250)
    product_type = models.ForeignKey('ProductType', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'product_model'


class Warranty(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=13)
    mail = models.EmailField(max_length=250)
    product_type = models.ForeignKey('ProductType', on_delete=models.SET_NULL, blank=True, null=True)
    model = models.ForeignKey('ProductModel', on_delete=models.SET_NULL, blank=True, null=True)
    serial_number = models.CharField(max_length=250)
    dealer_name = models.CharField(max_length=250, blank=True, null=True)
    invoice_date = models.DateField()
    invoice_number = models.CharField(max_length=250, blank=True, null=True)
    contact_person = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_created=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    billing_address1 = models.CharField(max_length=250, null=True)
    billing_address2 = models.CharField(max_length=250, null=True)
    billing_landmark = models.CharField(max_length=250, null=True)
    billing_state = models.ForeignKey(
        'user.State', on_delete=models.SET_NULL, related_name='billing_state', null=True, blank=True)
    billing_district = models.ForeignKey(
        'user.District', on_delete=models.SET_NULL, related_name='billing_district', null=True, blank=True)
    billing_pincode = models.ForeignKey(
        'user.CityPincode', on_delete=models.SET_NULL, related_name='billing_pincode', null=True, blank=True)
    installation_address1 = models.CharField(max_length=250, null=True)
    installation_address2 = models.CharField(max_length=250, null=True)
    installation_landmark = models.CharField(max_length=250, null=True)
    installation_state = models.ForeignKey(
        'user.State', on_delete=models.SET_NULL, related_name='installation_state', null=True, blank=True)
    installation_district = models.ForeignKey(
        'user.District', on_delete=models.SET_NULL, related_name='installation_district', null=True, blank=True)
    installation_pincode = models.ForeignKey(
        'user.CityPincode', on_delete=models.SET_NULL, related_name='installation_pincode', null=True, blank=True)
    image = models.FileField(max_length=250, blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'waranty'

    def __str__(self):
        return self.name


class Vendor(models.Model):
    id = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=250)
    page_heading = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    contact_name = models.CharField(max_length=250, blank=True, null=True)
    phone_code = models.IntegerField(blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    browser_title = models.CharField(max_length=250, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vendors'

    def __str__(self):
        return self.vendor_name


class Page(models.Model):
    id = models.BigAutoField(primary_key=True)
    slug = models.CharField(unique=True, max_length=255)
    type = models.CharField(max_length=7, choices=[
        ('Blog', 'Blog'),
        ('Career', 'Career'),
        ('Events', 'Events'),
        ('History', 'History'),
        ('News', 'News'),
        ('Page', 'Page')
    ], default='Page')
    event_date_time = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    primary_heading = models.CharField(max_length=255, blank=True, null=True)
    short_description = models.CharField(max_length=1000, blank=True, null=True)
    content = models.TextField()
    parent_id = models.BigIntegerField()
    media = models.ForeignKey('MediaLibrary', on_delete=models.SET_NULL, blank=True, null=True)
    banner = models.ForeignKey('cms.Banner', on_delete=models.SET_NULL, blank=True, null=True)
    browser_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    top_description = models.CharField(max_length=1000, blank=True, null=True)
    bottom_description = models.CharField(max_length=1000, blank=True, null=True)
    extra_css = models.CharField(max_length=1000, blank=True, null=True)
    extra_js = models.CharField(max_length=1000, blank=True, null=True)
    status = models.IntegerField()
    views = models.BigIntegerField()
    block_1_title = models.TextField(blank=True, null=True)
    block_1_summary = models.TextField(blank=True, null=True)
    block_2_title = models.TextField(blank=True, null=True)
    block_2_summary = models.TextField(blank=True, null=True)
    block_3_title = models.TextField(blank=True, null=True)
    block_3_summary = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        'user.User', on_delete=models.SET_NULL, db_column='created_by', blank=True, null=True,
        related_name='pages_created_by')
    updated_by = models.ForeignKey(
        'user.User', on_delete=models.SET_NULL, db_column='updated_by', blank=True, null=True,
        related_name='pages_updated_by')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pages'

    def __str__(self):
        return self.name

    def get_media_url(self):
        if self.media_id and self.media.file_path:
            return self.media.file_path.url


class Blocks(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=7)
    variant = models.ForeignKey('ProductVariant', on_delete=models.SET_NULL, blank=True, null=True)
    page = models.ForeignKey('Page', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'blocks'

    def __str__(self):
        return self.type


class ExtendedWarranties(models.Model):
    id = models.AutoField(primary_key=True)
    products = models.ForeignKey('Product', on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=250)
    warranty_price = models.FloatField()
    year = models.CharField(max_length=1)
    start_price = models.FloatField(blank=True, null=True)
    end_price = models.FloatField(blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'extended_warranties'

    def __str__(self):
        return self.title


class Slider(models.Model):
    id = models.AutoField(primary_key=True)
    slider_name = models.CharField(max_length=250)
    code = models.CharField(max_length=250)
    width = models.SmallIntegerField()
    height = models.SmallIntegerField()
    created_by = models.ForeignKey('user.User', on_delete=models.SET_NULL, db_column='created_by',
                                   blank=True, null=True, related_name='slider_created_by')
    updated_by = models.ForeignKey('user.User', on_delete=models.SET_NULL, db_column='updated_by',
                                   blank=True, null=True, related_name='slider_updated_by')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'sliders'

    def __str__(self):
        return self.slider_name


class SliderPhoto(models.Model):
    id = models.AutoField(primary_key=True)
    sliders = models.ForeignKey('Slider', on_delete=models.SET_NULL, blank=True, null=True)
    media = models.ForeignKey('MediaLibrary', on_delete=models.SET_NULL, blank=True, null=True)
    crop_data = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    alt_text = models.CharField(max_length=250, blank=True, null=True)
    button_text = models.CharField(max_length=250, blank=True, null=True)
    button_link = models.CharField(max_length=250, blank=True, null=True)
    button_link_target = models.CharField(max_length=10, blank=True, null=True)
    button2_text = models.CharField(max_length=250, blank=True, null=True)
    button2_link = models.CharField(max_length=250, blank=True, null=True)
    button2_link_target = models.CharField(max_length=20, blank=True, null=True)
    created_by = models.ForeignKey('user.User', on_delete=models.SET_NULL, db_column='created_by',
                                   blank=True, null=True, related_name='slider_photo_created_by')
    updated_by = models.ForeignKey('user.User', on_delete=models.SET_NULL,
                                   db_column='updated_by',
                                   blank=True, null=True, related_name='slider_photo_updated_by')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'slider_photos'

    def __str__(self):
        return self.title


class Search(models.Model):
    id = models.AutoField(primary_key=True)
    variant = models.ForeignKey('ProductVariant', on_delete=models.SET_NULL,
                                blank=True, null=True, related_name='search_variant')
    name = models.CharField(max_length=250)
    keyword = models.CharField(max_length=200)
    priority = models.IntegerField()
    type = models.CharField(max_length=8)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'search'

    def __str__(self):
        return self.name


class SearchHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('user.User', on_delete=models.SET_NULL, blank=True, null=True)
    search_term = models.CharField(max_length=250)
    count = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'search_history'

    def __str__(self):
        return self.search_term


class Settings(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=250)
    value = models.TextField(blank=True, null=True)
    media = models.ForeignKey('MediaLibrary', on_delete=models.SET_NULL, blank=True, null=True)
    type = models.CharField(max_length=20)
    page = models.CharField(max_length=250, blank=True, null=True)
    created_by = models.ForeignKey('user.User', on_delete=models.SET_NULL, db_column='created_by',
                                   blank=True, null=True, related_name='setting_created_by')
    updated_by = models.ForeignKey('user.User', on_delete=models.SET_NULL,
                                   db_column='updated_by',
                                   blank=True, null=True, related_name='setting_updated_by')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'settings'

    def __str__(self):
        return self.code

    def get_media_url(self):
        if self.media_id and self.media.file_path:
            return self.media.file_path.url


class Specifications(models.Model):
    id = models.AutoField(primary_key=True)
    variant = models.ForeignKey('ProductVariant', models.SET_NULL, blank=True, null=True)
    group = models.CharField(max_length=250, blank=True, null=True)
    key = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()
    batch = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'specifications'

    def __str__(self):
        return self.group

class Enquiry(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    mail = models.EmailField()
    place = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    district = models.CharField(max_length=250)
    phone = models.CharField(max_length=13)
    requirement = models.CharField(max_length=150)
    message = models.CharField(max_length=250)

    class Meta:
        managed = True
        db_table = 'enquiry'

    def __str__(self):
        return self.name

    def send_email_notifications(self):
        # Email user a thank-you note
        user_subject = 'WE value your enquiry'
        user_message = 'Dear {},\n\nThank you for your enquiry. We appreciate your interest in Hykon India Limited. Our team will review your information and get back to you shortly.\n\nBest regards,\nHykon India Limited'.format(
            self.name)
        send_mail(user_subject, user_message, settings.DEFAULT_FROM_EMAIL, [self.mail], fail_silently=True)

        # Notify admin about the new enquiry
        admin_subject = 'New Enquiry Received'
        admin_message = 'Dear Admin,\n\nA new enquiry has been received. Please find the details below:\n\nName: {}\nEmail: {}\nPlace: {}\nState: {}\nDistrict: {}\nPhone: {}\nRequirement: {}\nMessage: {}\n\nBest regards,\nHykon India Limited'.format(
            self.name, self.mail, self.place, self.state, self.district, self.phone, self.requirement, self.message)
        admin_email = settings.HYKON_EMAIL # Update with your admin email address
        send_mail(admin_subject, admin_message, settings.DEFAULT_FROM_EMAIL, [admin_email], fail_silently=True)