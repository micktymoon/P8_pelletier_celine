from django.test import TestCase
from website.models import Product, Category, Store


class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Cola',
            brand='Coca',
            nutri_score='e',
            url_off='https://off.fr/cola',
            url_image='https://image-cola.fr',
            nutriments_100g='{glucose_100g: 6}')

    def test_name_label(self):
        field_label = self.product._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_brand_label(self):
        field_label = self.product._meta.get_field('brand').verbose_name
        self.assertEquals(field_label, 'brand')

    def test_nutri_score_label(self):
        field_label = self.product._meta.get_field('nutri_score').verbose_name
        self.assertEquals(field_label, 'nutri score')

    def test_url_off_label(self):
        field_label = self.product._meta.get_field('url_off').verbose_name
        self.assertEquals(field_label, 'url off')

    def test_url_image_label(self):
        field_label = self.product._meta.get_field('url_image').verbose_name
        self.assertEquals(field_label, 'url image')

    def test_nutriments_100g_label(self):
        field_label = self.product._meta.get_field(
            'nutriments_100g').verbose_name
        self.assertEquals(field_label, 'nutriments 100g')

    def test_name_max_length(self):
        max_length = self.product._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

    def test_brand_max_length(self):
        max_length = self.product._meta.get_field('brand').max_length
        self.assertEquals(max_length, 255)

    def test_nutri_score_max_length(self):
        max_length = self.product._meta.get_field('nutri_score').max_length
        self.assertEquals(max_length, 2)

    def test_unique_together(self):
        with self.assertRaises(Exception):
            Product.objects.create(name='Cola',
                                   brand='Coca',
                                   nutri_score='e',
                                   url_off='https://off.fr/cola',
                                   url_image='https://image-cola.fr',
                                   nutriments_100g='{glucose_100g: 6}')


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name_cat='Boissons')

    def test_name_cat_label(self):
        field_label = self.category._meta.get_field('name_cat').verbose_name
        self.assertEquals(field_label, 'name cat')

    def test_name_cat_max_length(self):
        max_length = self.category._meta.get_field('name_cat').max_length
        self.assertEquals(max_length, 255)


class StoreModelTest(TestCase):
    def setUp(self):
        self.store = Store.objects.create(name_store='Auchan')

    def test_name_store_label(self):
        field_label = self.store._meta.get_field('name_store').verbose_name
        self.assertEquals(field_label, 'name store')

    def test_name_store_max_length(self):
        max_length = self.store._meta.get_field('name_store').max_length
        self.assertEquals(max_length, 255)
