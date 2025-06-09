from django.urls import path
from .views import ProductoListView, ProductoCreateView, ProductoDetailView, ProductoDeleteView

urlpatterns = [
    path('', ProductoListView.as_view(), name='listado'),
    path('agregar/', ProductoCreateView.as_view(), name='agregar'),
    path('<slug:slug>/', ProductoDetailView.as_view(), name='detalle'),
    path('eliminar/<slug:slug>/', ProductoDeleteView.as_view(), name='eliminar'),
]