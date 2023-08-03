from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'states'

    def __str__(self):
        return self.name


class District(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.ForeignKey('State', on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'districts'

    def __str__(self):
        return self.name


class City(models.Model):
    id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=100)
    state = models.ForeignKey('State', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'city'

    def __str__(self):
        return self.city_name


class CityPincode(models.Model):
    id = models.AutoField(primary_key=True)
    district = models.ForeignKey('District', on_delete=models.SET_NULL, null=True, blank=True)
    place = models.CharField(max_length=50, blank=True, null=True)
    pin_code = models.CharField(max_length=50, blank=True, null=True)
    is_available = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'city_pincodes'

    def __str__(self):
        return self.pin_code


class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    # username = models.CharField(max_length=250, blank=True, null=True)
    # first_name = models.CharField(max_length=250, blank=True, null=True)
    # last_name = models.CharField(max_length=250, blank=True, null=True)
    # email = models.CharField(unique=True, max_length=191, blank=True, null=True)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    phone_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=191, blank=True, null=True)
    otp = models.IntegerField(blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    country_code = models.IntegerField(blank=True, null=True)
    phone_number = models.BigIntegerField(blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True)
    pin_code = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    banned_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    password_resets = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'users'

    def __str__(self):
        return str(self.id)

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.SET_NULL, blank=True, null=True, related_name='user_address')
    full_name = models.CharField(max_length=100)
    mobile_code = models.IntegerField(default=91)
    mobile_number = models.CharField(max_length=100)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250, blank=True, null=True)
    landmark = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True)
    country_id = models.IntegerField(default=101)
    pincode = models.IntegerField()
    type = models.CharField(max_length=1, choices=[
        ('1', 'Home'),
        ('0', 'Office')
    ])
    delivery_instructions = models.TextField(blank=True, null=True)
    is_default = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'address'
