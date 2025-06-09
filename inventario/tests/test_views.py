from django.test import TestCase, Client
from django.urls import reverse
from inventario.models import Producto

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.producto = Producto.objects.create(
            nombre="Mouse",
            categoria="Periférico",
            cantidad=5,
            precio=15000
        )

    def test_producto_list_status_code(self):
        response = self.client.get(reverse('listado'))
        self.assertEqual(response.status_code, 404) 

    def test_producto_create_view(self):
        response = self.client.post(reverse('agregar'), {
            'nombre': 'Teclado',
            'categoria': 'Periférico',
            'cantidad': 10,
            'precio': 25000
        })
        self.assertEqual(response.status_code, 302)

    def test_producto_detail_view(self):
        response = self.client.get(reverse('detalle', args=[self.producto.slug]))
        self.assertTemplateUsed(response, 'inventario/detalle.html') 