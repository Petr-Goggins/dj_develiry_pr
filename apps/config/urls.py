from apps.catalog.views import get_catalog

from django.urls import path,include

urlpatterns = [
    path('', get_catalog),
]
