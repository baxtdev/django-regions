from rest_framework import serializers

from apps.country.models import Country,City,Region


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
       

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    class Meta:
        model = Region
        fields = '__all__'


class ListRegionSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    cities = CitySerializer(many=True, read_only=True)

    class Meta:
        model = Region
        fields = '__all__'


class ListCountrySerializer(serializers.ModelSerializer):
    regions = ListRegionSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = '__all__'


class ListCitySerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)
    class Meta:
        model = City
        fields = '__all__'


