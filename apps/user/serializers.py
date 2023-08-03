from rest_framework import serializers
from .models import District, CityPincode
from apps.catalogue.models import ProductModel


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'state']


class PincodeSerializer(serializers.ModelSerializer):
    district = DistrictSerializer()

    class Meta:
        model = CityPincode
        fields = ['id', 'district']


class ProductModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = '__all__'
