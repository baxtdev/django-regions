from rest_framework import routers
from django.urls import include, path
from api.country.endpoints import urlpatterns

from .yasg import urlpatterns as url_doc


urlpatterns=[
    path('',include(urlpatterns)),
]

urlpatterns+=url_doc