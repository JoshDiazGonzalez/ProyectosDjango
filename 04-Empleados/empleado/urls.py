from django.contrib import admin
from django.urls import path, include, re_path
from applications.home.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.home.urls')),
    #incluimos la url de la app departamento
    re_path('', include('applications.empleados.urls')),
]
