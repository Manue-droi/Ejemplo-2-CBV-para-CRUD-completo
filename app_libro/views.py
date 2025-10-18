from django.views.generic import ListView
from .models import Libro

class LibroListView(ListView):
    model = Libro
    template_name = "app_libro/lista.html"
    context_object_name = "libros"
