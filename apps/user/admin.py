from django.contrib import admin
from .models import *


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'email', 'phone_number')


admin.site.register(User, UsersAdmin)
admin.site.register(State)
admin.site.register(District)
admin.site.register(City)
admin.site.register(CityPincode)
admin.site.register(Address)
