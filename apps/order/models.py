from django.db import models


# Create your models here.


class Wishlist(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('user.User', on_delete=models.SET_NULL, blank=True, null=True)
    variant = models.ForeignKey('catalogue.ProductVariant', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'wishlist'

    def __str__(self):
        return str(self.user_id)


class Offer(models.Model):
    id = models.BigAutoField(primary_key=True)
    vendor = models.ForeignKey('catalogue.Vendor', on_delete=models.SET_NULL, blank=True, null=True)
    slug = models.CharField(max_length=250, blank=True, null=True)
    offer_name = models.CharField(max_length=250)
    type = models.CharField(max_length=10)
    validity_start_date = models.DateField()
    validity_end_date = models.DateField()
    applicable_for_full_order = models.IntegerField()
    discount_type = models.CharField(max_length=20, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    percentage = models.IntegerField(blank=True, null=True)
    min_purchase_amount = models.FloatField(blank=True, null=True)
    max_discount_amount = models.FloatField(blank=True, null=True)
    is_active = models.IntegerField()
    browser_title = models.CharField(max_length=250, blank=True, null=True)
    meta_description = models.CharField(max_length=250, blank=True, null=True)
    meta_keywords = models.CharField(max_length=520, blank=True, null=True)
    created_by = models.ForeignKey('user.User', on_delete=models.SET_NULL,
                                   db_column='created_by', blank=True, null=True, related_name='offers_created_by')
    updated_by = models.ForeignKey('user.User', on_delete=models.SET_NULL,
                                   db_column='updated_by', blank=True, null=True, related_name='offers_updated_by')
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'offers'


class OfferCategory(models.Model):
    id = models.AutoField(primary_key=True)
    categories = models.ForeignKey('catalogue.Category', on_delete=models.SET_NULL, blank=True, null=True)
    offers = models.ForeignKey('Offer', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = True
        db_table = 'offer_categories'

    def __str__(self):
        return self.categories_id


class OfferComboFreeProduct(models.Model):
    id = models.AutoField(primary_key=True)
    products = models.ForeignKey('catalogue.Product', on_delete=models.SET_NULL, blank=True, null=True)
    offers = models.ForeignKey('Offer', on_delete=models.SET_NULL, blank=True, null=True)
    type = models.CharField(max_length=20)
    fixed_price = models.FloatField(blank=True, null=True)
    discount_amount = models.FloatField(blank=True, null=True)
    discount_percentage = models.IntegerField(blank=True, null=True)
    max_discount_amount = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = True
        db_table = 'offer_combo_free_products'

    def __str__(self):
        return self.products_id


class OfferComboProduct(models.Model):
    id = models.AutoField(primary_key=True)
    products = models.ForeignKey('catalogue.Product', on_delete=models.SET_NULL, blank=True, null=True)
    offers = models.ForeignKey('Offer', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = True
        db_table = 'offer_combo_products'

    def __str__(self):
        return self.products_id


class OfferGroup(models.Model):
    id = models.AutoField(primary_key=True)
    groups = models.ForeignKey('catalogue.Group', on_delete=models.SET_NULL, blank=True, null=True)
    offers = models.ForeignKey('Offer', on_delete=models.SET_NULL, blank=True, null=True)
    how_many_to_buy = models.IntegerField()
    how_many_to_get_free = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = True
        db_table = 'offer_groups'

    def __str__(self):
        return self.groups_id


class OfferPriceProduct(models.Model):
    id = models.AutoField(primary_key=True)
    products = models.ForeignKey('catalogue.Product', on_delete=models.SET_NULL, blank=True, null=True)
    offers = models.ForeignKey('Offer', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = True
        db_table = 'offer_price_products'

    def __str__(self):
        return self.products_id


class Coupon(models.Model):
    id = models.AutoField(primary_key=True)
    coupon_code = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    minimum_purchase_value = models.FloatField()
    discount_type = models.CharField(max_length=20)
    discount_percentage = models.IntegerField(blank=True, null=True)
    discount_amount = models.FloatField(blank=True, null=True)
    maximum_discount_value = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    terms = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created_by = models.ForeignKey(
        'user.User', on_delete=models.SET_NULL, db_column='created_by', blank=True, null=True,
        related_name='coupons_created_by')
    updated_by = models.ForeignKey(
        'user.User', on_delete=models.SET_NULL, db_column='updated_by', blank=True, null=True,
        related_name='coupons_updated_by')
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'coupons'

    def __str__(self):
        return self.coupon_code


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=17, default='payment_started', choices=[
        ('payment_started', 'Payment Started'),
        ('payment_completed', 'Payment Completed'),
        ('cod', 'Cash On Delivery')
    ])
    users = models.ForeignKey('user.User', on_delete=models.SET_NULL, blank=True, null=True)
    transaction_id = models.CharField(max_length=150)
    coupon = models.ForeignKey('Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    coupon_discount = models.FloatField(blank=True, null=True)
    order_reference_number = models.CharField(max_length=150)
    total_mrp = models.FloatField()
    total_discount = models.FloatField()
    total_sale_price = models.FloatField()
    total_final_price = models.FloatField()
    payment_method = models.CharField(max_length=250, default='online', choices=[
        ('cod', 'Cash On Delivery'),
        ('online', 'Online')
    ])
    payment_status = models.BooleanField(default=False)
    payment_receive_status = models.BooleanField(default=False)
    delivery_address_id = models.ForeignKey('user.Address', on_delete=models.SET_NULL, null=True, blank=True)
    delivery_instructions = models.TextField(blank=True, null=True)
    response_data = models.TextField(blank=True, null=True)
    is_cancelled = models.BooleanField(default=False)
    cancelled_reason = models.TextField(blank=True, null=True)
    other_reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    placed = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'orders'

    def __str__(self):
        return str(self.id)


class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    orders = models.ForeignKey('Order', on_delete=models.SET_NULL, blank=True, null=True)
    products = models.ForeignKey('catalogue.ProductVariant', on_delete=models.SET_NULL, blank=True, null=True)
    cart_offer = models.ForeignKey('OfferGroup', on_delete=models.SET_NULL, blank=True, null=True)
    offer_parent = models.ForeignKey('Offer', on_delete=models.SET_NULL, db_column='offer_parent', blank=True, null=True)
    product_offer = models.ForeignKey('OfferPriceProduct', on_delete=models.SET_NULL, blank=True, null=True)
    mrp = models.FloatField()
    quantity = models.IntegerField()
    sale_price = models.FloatField()
    price = models.FloatField()
    discount = models.FloatField()
    expected_delivery_date = models.DateField(blank=True, null=True)
    customer_instructions = models.TextField(blank=True, null=True)
    # waranty = models.ForeignKey('catalogue.Warranty', on_delete=models.SET_NULL, blank=True, null=True)
    # warranty_parent = models.IntegerField(blank=True, null=True)
    is_returned = models.BooleanField(default=False)
    returned_reason = models.TextField(blank=True, null=True)
    is_cancelled = models.BooleanField(default=False)
    cancelled_reason = models.TextField(blank=True, null=True)
    other_reason = models.TextField(blank=True, null=True)
    refund_request_id = models.CharField(max_length=250, blank=True, null=True)
    status = models.ForeignKey('OrderStatusLabelsMaster', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'order_details'

    def __str__(self):
        return str(self.id)


class OrderStatusLabelsMaster(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    display_order = models.IntegerField()
    color_code = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'order_status_labels_master'

    def __str__(self):
        return self.name


class OrderTracking(models.Model):
    id = models.AutoField(primary_key=True)
    order_details = models.ForeignKey(
        'OrderDetail', on_delete=models.SET_NULL, blank=True, null=True)
    order_status_labels_master = models.ForeignKey(
        'OrderStatusLabelsMaster', on_delete=models.SET_NULL, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        'user.User', on_delete=models.SET_NULL, db_column='created_by', blank=True, null=True,
        related_name='order_tracking_created_by')
    updated_by = models.ForeignKey(
        'user.User', on_delete=models.SET_NULL, db_column='updated_by', blank=True, null=True,
        related_name='order_tracking_updated_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'order_tracking'

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    # warranty_parent = models.ForeignKey(
    #     'catalogue.Warranty', on_delete=models.SET_NULL, db_column='warranty_parent', blank=True, null=True)
    offer_parent = models.ForeignKey('Offer', on_delete=models.SET_NULL, db_column='offer_parent', blank=True, null=True)
    user = models.ForeignKey('user.User', on_delete=models.SET_NULL, blank=True, null=True)
    product_offer = models.ForeignKey('OfferPriceProduct', on_delete=models.SET_NULL, blank=True, null=True)
    cart_offer = models.ForeignKey('OfferGroup', on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey('catalogue.ProductVariant', on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField()
    price = models.FloatField(blank=True, null=True)
    retail_price = models.FloatField(blank=True, null=True)
    sale_price = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    placed = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'cart'

    def __str__(self):
        return str(self.user_id)


class CancelOrderReason(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    display_order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cancel_order_reasons'

    def __str__(self):
        return self.title
