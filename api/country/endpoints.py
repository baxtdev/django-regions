from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import CountryViewSet, RegionViewSet, CityViewSet

router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'regions', RegionViewSet)
router.register(r'cities', CityViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
