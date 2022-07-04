from django.test import TestCase
from inventory.models.brand import Brand


class TestModel(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name = "Tesla")

    def test_create_brand(self):
        self.assertEquals(self.brand.name, "Tesla")