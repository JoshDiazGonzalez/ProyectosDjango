from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    #incluimos la url de la app departamento
    re_path('', include('applications.home.urls')),
    re_path('', include('applications.empleados.urls')),
    re_path('', include('applications.departamento.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
