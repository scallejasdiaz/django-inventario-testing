from django.test import TestCase
from inventario.models import Producto

class TestModels(TestCase):

    def test_slug_no_se_genero(self):
        producto = Producto.objects.create(
            nombre="Monitor",
            categoria="Pantallas",
            cantidad=3,
            precio=120000
        )
        self.assertIsNotNone(producto.slug)  