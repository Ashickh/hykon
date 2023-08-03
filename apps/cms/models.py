from django.db import models


class Banner(models.Model):
    id = models.AutoField(primary_key=True)
    banner_name = models.CharField(max_length=250)
    title = models.CharField(max_length=250, blank=True, null=True)
    code = models.CharField(max_length=250)
    width = models.SmallIntegerField(blank=True, null=True)
    height = models.SmallIntegerField(blank=True, null=True)
    link = models.CharField(max_length=250, blank=True, null=True)
    created_by = models.ForeignKey(
        'user.User', on_delete=models.SET_NULL, db_column='created_by', blank=True, null=True,
        related_name='banners_created_by')
    updated_by = models.ForeignKey(
        'user.User', on_delete=models.SET_NULL, db_column='updated_by', blank=True, null=True,
        related_name='banners_updated_by')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.banner_name

    class Meta:
        managed = True
        db_table = 'banners'


class BannerPhoto(models.Model):
    id = models.AutoField(primary_key=True)
    banners = models.ForeignKey('Banner', on_delete=models.SET_NULL, blank=True, null=True)
    media = models.ForeignKey('catalogue.MediaLibrary', on_delete=models.SET_NULL, blank=True, null=True)
    crop_data = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    alt_text = models.CharField(max_length=250, blank=True, null=True)
    link = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.banners.banner_name

    class Meta:
        managed = True
        db_table = 'banner_photos'

    def get_media_url(self):
        if self.media_id and self.media.file_path:
            return self.media.file_path.url


class Bans(models.Model):
    id = models.AutoField(primary_key=True)
    bannable_type = models.CharField(max_length=191)
    bannable = models.ForeignKey('Banner', on_delete=models.SET_NULL, blank=True, null=True)
    created_by_type = models.CharField(max_length=191, blank=True, null=True)
    created_by = models.ForeignKey('user.User', on_delete=models.SET_NULL, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    expired_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = True
        db_table = 'bans'


class BranchData(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=46, blank=True, null=True)
    city = models.CharField(max_length=91, blank=True, null=True)
    district = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=11, blank=True, null=True)
    mobile = models.CharField(max_length=35, blank=True, null=True)
    contact = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'brach_data'


class BranchLandmark(models.Model):
    id = models.AutoField(primary_key=True)
    landmark = models.CharField(max_length=50)
    district = models.ForeignKey('user.District', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.landmark

    class Meta:
        managed = True
        db_table = 'branch_landmarks'


class Branches(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=7)
    state = models.ForeignKey('user.State', on_delete=models.SET_NULL, blank=True, null=True)
    district = models.ForeignKey('user.District', on_delete=models.SET_NULL, blank=True, null=True)
    location = models.CharField(max_length=250)
    branch_name = models.CharField(max_length=250)
    page_heading = models.CharField(max_length=500, blank=True, null=True)
    slug = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    landline_number = models.CharField(max_length=50, blank=True, null=True)
    contact_person = models.CharField(max_length=250, blank=True, null=True)
    contact_person_number = models.CharField(max_length=50, blank=True, null=True)
    contact_person_image = models.IntegerField(blank=True, null=True)
    landmark = models.ForeignKey('BranchLandmark', on_delete=models.SET_NULL, blank=True, null=True)
    gstin = models.CharField(db_column='GSTIN', max_length=45, blank=True, null=True)  # Field name made lowercase.
    media = models.ForeignKey('catalogue.MediaLibrary', on_delete=models.SET_NULL, blank=True, null=True)
    banner = models.ForeignKey('Banner', on_delete=models.SET_NULL, blank=True, null=True)
    lattitude = models.CharField(max_length=191, blank=True, null=True)
    longitude = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    mobile_number = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    sunday_open = models.IntegerField()
    browser_title = models.CharField(max_length=250, blank=True, null=True)
    meta_description = models.CharField(max_length=500, blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)
    status = models.IntegerField()
    created_by = models.ForeignKey(
        'user.User', on_delete=models.SET_NULL, db_column='created_by', blank=True, null=True,
        related_name='branches_created_by')
    updated_by = models.ForeignKey(
        'user.User', on_delete=models.SET_NULL, db_column='updated_by', blank=True, null=True,
        related_name='branches_updated_by')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.branch_name

    class Meta:
        managed = True
        db_table = 'branches'


class FrontendPage(models.Model):
    id = models.BigAutoField(primary_key=True)
    slug = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    media = models.ForeignKey('catalogue.MediaLibrary', on_delete=models.SET_NULL, blank=True, null=True)
    browser_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    top_description = models.CharField(max_length=1000, blank=True, null=True)
    bottom_description = models.CharField(max_length=1000, blank=True, null=True)
    extra_css = models.CharField(max_length=1000, blank=True, null=True)
    extra_js = models.CharField(max_length=1000, blank=True, null=True)
    status = models.IntegerField()
    created_by = models.ForeignKey(
        'user.User', on_delete=models.SET_NULL, db_column='created_by', blank=True, null=True,
        related_name='frontend_pages_created_by')
    updated_by = models.ForeignKey(
        'user.User', on_delete=models.SET_NULL, db_column='updated_by', blank=True, null=True,
        related_name='frontend_pages_updated_by')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'frontend_pages'


class HomePageSetting(models.Model):
    id = models.AutoField(primary_key=True)
    section = models.CharField(max_length=250)
    code = models.CharField(max_length=250)
    type = models.CharField(max_length=10)
    content = models.TextField()
    created_by = models.ForeignKey(
        'user.User', on_delete=models.SET_NULL, db_column='created_by', blank=True, null=True,
        related_name='home_page_settings_created_by')
    updated_by = models.ForeignKey(
        'user.User', on_delete=models.SET_NULL, db_column='updated_by', blank=True, null=True,
        related_name='home_page_settings_updated_by')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.section

    class Meta:
        managed = True
        db_table = 'home_page_settings'


class Menu(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    position = models.CharField(max_length=255)
    menu_type = models.IntegerField()
    menu_order = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    created_by = models.ForeignKey('user.User', on_delete=models.SET_NULL,
                                   db_column='created_by', blank=True, null=True, related_name='menus_created_by')
    updated_by = models.ForeignKey('user.User', on_delete=models.SET_NULL,
                                   db_column='updated_by', blank=True, null=True, related_name='menus_updated_by')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'menus'


class MenuItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    menu = models.ForeignKey('Menu', on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255, blank=True, null=True)
    menu_type = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    menu_nextable_id = models.CharField(max_length=255, blank=True, null=True)
    linkable_type = models.CharField(max_length=191, blank=True, null=True)
    linkable_id = models.PositiveBigIntegerField(blank=True, null=True)
    menu_order = models.IntegerField()
    parent_id = models.BigIntegerField()
    target_blank = models.IntegerField()
    created_by = models.ForeignKey('user.User', on_delete=models.SET_NULL,
                                   db_column='created_by', blank=True, null=True, related_name='menu_items_created_by')
    updated_by = models.ForeignKey('user.User', on_delete=models.SET_NULL,
                                   db_column='updated_by', blank=True, null=True, related_name='menu_items_updated_by')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        db_table = 'menu_items'


class NewsletterSubscription(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=250)
    unsubscribed = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.email

    class Meta:
        managed = True
        db_table = 'newsletter_subscriptions'


class PasswordReset(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=191)
    token = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        managed = True
        db_table = 'password_resets'


class Activitie(models.Model):
    id = models.BigAutoField(primary_key=True)
    request_token = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('user.User', models.SET_NULL, blank=True, null=True)
    guest_id = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=50, blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    response_http_code = models.CharField(max_length=255, blank=True, null=True)
    response_time = models.CharField(max_length=255, blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    payload = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = True
        db_table = 'activities'


class AdminPage(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    permission = models.CharField(max_length=250)
    target = models.CharField(max_length=10, blank=True, null=True)
    icon = models.CharField(max_length=50)
    parent = models.IntegerField()
    display_order = models.IntegerField()
    created_by = models.BigIntegerField()
    updated_by = models.BigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        db_table = 'admin_pages'
