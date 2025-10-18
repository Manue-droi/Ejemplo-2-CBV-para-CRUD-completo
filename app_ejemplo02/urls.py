from django.urls import path
from .views import (
    LibroListView, LibroDetailView, LibroCreateView,
    LibroUpdateView, LibroDeleteView
)

urlpatterns = [
    path("ejemplo02/",LibroListView.as_view(), name="libro_list"),
    path("ejemplo02/<int:pk>/", LibroDetailView.as_view(), name="libro_detail"),
    path("ejemplo02/nuevo/", LibroCreateView.as_view(), name="libro_create"),
    path("ejemplo02/<int:pk>/editar/", LibroUpdateView.as_view(), name="libro_update"),
    path("ejemplo02/<int:pk>/eliminar/", LibroDeleteView.as_view(), name="libro_delete"),
]
