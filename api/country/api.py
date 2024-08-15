from rest_framework import viewsets
from rest_framework.filters import SearchFilter,OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CountrySerializer,ListCountrySerializer,Country,\
    RegionSerializer,ListRegionSerializer,Region,\
    CitySerializer,ListCitySerializer,City

class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = ListCountrySerializer
    filter_backends = [SearchFilter,DjangoFilterBackend]
    search_fields = ['name','regions__name','regions__cities__name']


class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Region.objects.all()
    serializer_class = ListRegionSerializer
    filter_backends = [SearchFilter,DjangoFilterBackend]
    search_fields = ['name','country__name']
    filterset_fields = ['country']


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = ListCitySerializer
    filter_backends = [SearchFilter,DjangoFilterBackend]
    search_fields = ['name','region__name','region__country__name']
    filterset_fields = ['region']
    
