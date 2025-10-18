from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app_libro.models import Libro

class LibroListView(ListView):
    model = Libro
    template_name = "app_ejemplo02/libro_list.html"
    context_object_name = "libros"

class LibroDetailView(DetailView):
    model = Libro
    template_name = "app_ejemplo02/libro_detail.html"
    context_object_name = "libro"

class LibroCreateView(CreateView):
    model = Libro
    fields = ["titulo", "autor"]
    template_name = "app_ejemplo02/libro_form.html"
    success_url = reverse_lazy("libro_list")
    

class LibroUpdateView(UpdateView):
    model = Libro
    fields = ["titulo", "autor"]
    template_name = "app_ejemplo02/libro_form.html"
    success_url = reverse_lazy("libro_list")
    

class LibroDeleteView(DeleteView):
    model = Libro
    template_name = "app_ejemplo02/libro_confirm_delete.html"
    success_url = reverse_lazy("libro_list")
