from django.test import TestCase
from .models import Plan
from django.contrib.auth.models import User
# Create your tests here.

class PlanesTestCase(TestCase):
    def setUp(self):
        Plan.objects.create(name="Guantelete del infinito", review="El plan más poderoso del universo",
        description="5G acceso total: 5G Nationwide, 5G Ultra Wideband Plan features: 150 GB  of 5G Nationwide, 4G LTE data, 300 minutos",
        price="50")
        Plan.objects.create(name="Llamame y te llamo", review="El plan más poderoso del universo",
        description="5G acceso total: 5G Nationwide, 5G Ultra Wideband Plan features: 50 GB  of 5G Nationwide, 4G LTE data, 1500 minutos",
        price="30")
    
    def test_view_price(self):
        Guantelete = Plan.objects.get(name="Guantelete del infinito")

        self.assertEquals(Guantelete.price, 50)

    def test_view_price(self):
        Habla = Plan.objects.get(name="Llamame y te llamo")

        self.assertEquals(Habla.price, 31)

    