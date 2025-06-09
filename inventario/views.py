from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Producto

class ProductoListView(ListView):
    model = Producto
    template_name = 'listado.html'  

class ProductoCreateView(CreateView):
    model = Producto
    fields = ['nombre', 'categoria', 'cantidad', 'precio']
    template_name = 'formulario.html'



class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'detalle.html'

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'detalle.html'

