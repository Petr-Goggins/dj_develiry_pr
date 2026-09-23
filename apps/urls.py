
from django.contrib import admin
from apps.catalog.views import my_viev
from django.urls import path,include

app_name='catalog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', my_viev),
    path('hello/<int:id>', get_by_id),
    path('hello/<str:name>', my_viev),

    path('catalog/', get_catalog, name='catalog'),
]
