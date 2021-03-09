from django.test import TestCase
from django.urls import reverse

from website.models import Product, User


class HomeViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'home.html')


class LegalNoticeViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/mentionslegales/')
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        response = self.client.get(reverse('legal_notice'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('legal_notice'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'legal_notice.html')


class AccountViewTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='testuser',
                                                  password='testpassword',
                                                  email='testuser@email.fr')
        self.test_user.save()

    def test_account_view_uses_correct_user(self):
        login = self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('account'))

        self.assertEqual(str(response.context['user']), 'testuser')
        self.assertEqual(response.status_code, 200)

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('account'))

        self.assertEqual(str(response.context['user']), 'testuser')
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'account.html')


class ProductViewTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Cola',
                                              brand='Coca',
                                              nutri_score='e',
                                              url_off='https://off.fr/cola',
                                              url_image=
                                              'https://image-cola.fr',
                                              nutriments_100g=
                                              '{glucose_100g: 6}')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(f'/detail/{self.product.id}/')
        self.assertEqual(response.status_code, 200)

    def test_logged_in_uses_correct_template(self):
        response = self.client.get(f'/detail/{self.product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'detail.html')


class MyProductViewTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='testuser',
                                                  password='testpassword',
                                                  email='testuser@email.fr')
        self.test_user.save()

        number_of_products = 23

        for product_id in range(number_of_products):
            Product.objects.create(
                name=f'Coca {product_id}',
                nutri_score='e',
            )
        products = Product.objects.all()
        for product in products:
            self.test_user.product.add(product)

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/mesaliments/')
        self.assertEqual(str(response.context['user']), 'testuser')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        login = self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('my_product'))
        self.assertEqual(str(response.context['user']), 'testuser')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        login = self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('my_product'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'list_product.html')

    def test_pagination_is_twenty(self):
        login = self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('my_product'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertTrue(len(response.context['products']) == 20)

    def test_show_user_products(self):
        login = self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('my_product'))

        self.assertEqual(str(response.context['user']), 'testuser')
        self.assertEqual(response.status_code, 200)

        self.assertTrue('products' in response.context)
        self.assertEqual(len(response.context['products']), 20)
        shown_id = set(p.id for p in response.context["products"])
        self.assertTrue(self.test_user.product.first().id in shown_id)


class SaveViewTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='testuser',
                                                  password='testpassword',
                                                  email='testuser@email.fr')
        self.test_user.save()

        self.product = Product.objects.create(name='Cola',
                                              brand='Coca',
                                              nutri_score='e',
                                              url_off='https://off.fr/cola',
                                              url_image=
                                              'https://image-cola.fr',
                                              nutriments_100g=
                                              '{glucose_100g: 6}')

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(username='testuser', password='testpassword')
        response = self.client.get(f'/sauvegarde/{self.product.id}/')
        self.assertEqual(response.status_code, 302)

    def test_view_save_product_user(self):
        login = self.client.login(username=self.test_user.username, password='testpassword')
        response = self.client.get(f'/sauvegarde/{self.product.id}/')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.product in self.test_user.product.all())
        self.assertTrue(response.url.startswith(f'/detail/{self.product.id}'))

    def test_view_redirect_to_signup_if_no_logged_in(self):
        response = self.client.get(f'/sauvegarde/{self.product.id}/')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(f'/signup/'))