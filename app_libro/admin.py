from django.contrib import admin

# Register your models here.
from .models import Libro

admin.site.register(Libro)
# archivo: prj_sesion13/urls.py
from django.contrib import admin
from django.urls import path, include  # importar include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_hola.urls')),  # incluir las URLs de la app
    path('', include('app_info.urls')),
    path('', include('app_estudiante.urls')),  # incluir las URLs de la app
    path('', include('app_saludo.urls')),  # incluir las URLs de la app
    path('', include('app_libro.urls')),  # incluir las URLs de la app
]
