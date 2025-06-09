from django.test import SimpleTestCase
from django.urls import reverse, resolve
from inventario.views import ProductoListView

class TestUrls(SimpleTestCase):

    def test_url_listado_resuelve(self):
        url = reverse('listado')  
        self.assertEqual(resolve(url).func.view_class, ProductoListView)