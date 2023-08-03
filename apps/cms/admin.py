from django.contrib import admin
from .models import *


class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_name')


admin.site.register(Banner, BannerAdmin)


class BannerPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'crop_data', 'title', 'alt_text')
    search_fields = ('title', 'crop_data', 'alt_text')


admin.site.register(BannerPhoto, BannerPhotoAdmin)


class BansAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(Bans, BansAdmin)


class BranchDataAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(BranchData, BranchDataAdmin)


class BranchLandmarkAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(BranchLandmark, BranchLandmarkAdmin)


class BranchesAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(Branches, BranchesAdmin)


class FrontendPageAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(FrontendPage, FrontendPageAdmin)


class HomePageSettingAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(HomePageSetting, HomePageSettingAdmin)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Menu, MenuAdmin)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'menu', 'parent_id')


admin.site.register(MenuItem, MenuItemAdmin)


class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'unsubscribed')


admin.site.register(NewsletterSubscription, NewsletterSubscriptionAdmin)


class PasswordResetAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(PasswordReset, PasswordResetAdmin)


class ActivitieAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(Activitie, ActivitieAdmin)


class AdminPageAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(AdminPage, AdminPageAdmin)
