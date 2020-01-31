from django.test import TestCase
from library.models import Province
# Create your tests here.


class ProvinceTestCase(TestCase):

    def setUp(self):
        Province.objects.create(name='Adana')
        Province.objects.create(name='Adıyaman')
        Province.objects.create(name='Afyon')
        Province.objects.create(name='Ağrı')
        Province.objects.create(name='Amasya')
        Province.objects.create(name='Ankara')
