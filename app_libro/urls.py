from django.urls import path
from .views import LibroListView

urlpatterns = [
    path("libros/", LibroListView.as_view(), name="lista_libros"),
]
