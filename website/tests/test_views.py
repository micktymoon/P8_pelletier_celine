from django.core import mail
from django.test import TestCase
from django.urls import reverse

from website.models import Product, User, Category


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
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('account'))

        self.assertEqual(str(response.context['user']), 'testuser')
        self.assertEqual(response.status_code, 200)

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('account'))

        self.assertEqual(str(response.context['user']), 'testuser')
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'account.html')


class ProductViewTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Cola',
            brand='Coca',
            nutri_score='e',
            url_off='https://off.fr/cola',
            url_image='https://image-cola.fr',
            nutriments_100g='{glucose_100g: 6}')

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
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/mesaliments/')
        self.assertEqual(str(response.context['user']), 'testuser')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('my_product'))
        self.assertEqual(str(response.context['user']), 'testuser')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('my_product'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'list_product.html')

    def test_pagination_is_twenty(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('my_product'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertTrue(len(response.context['products']) == 20)

    def test_show_user_products(self):
        self.client.login(username='testuser', password='testpassword')
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

        self.product = Product.objects.create(
            name='Cola',
            brand='Coca',
            nutri_score='e',
            url_off='https://off.fr/cola',
            url_image='https://image-cola.fr',
            nutriments_100g='{glucose_100g: 6}')

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(f'/sauvegarde/{self.product.id}/')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(f'/detail/{self.product.id}'))

    def test_view_save_product_user(self):
        self.client.login(username=self.test_user.username,
                          password='testpassword')
        response = self.client.post(f'/sauvegarde/{self.product.id}/')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.product in self.test_user.product.all())
        self.assertTrue(response.url.startswith(f'/detail/{self.product.id}'))

    def test_view_redirect_to_signup_if_no_logged_in(self):
        response = self.client.post(f'/sauvegarde/{self.product.id}/')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/login/'))

    def test_method_get_not_save_product(self):
        self.client.login(username=self.test_user.username,
                          password='testpassword')
        response = self.client.get(f'/sauvegarde/{self.product.id}/')
        self.assertEqual(response.status_code, 405)


class SignupViewTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='testuser',
                                                  password='testpassword',
                                                  email='testuser@email.fr')
        self.test_user.save()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)

    def test_post_save_user_and_redirect_to_home(self):
        response = self.client.post('/signup/',
                                    data={'username': 'testusername',
                                          'first_name': 'testfirstname',
                                          'last_name': 'testlastname',
                                          'email': 'test@email.com',
                                          'password1': 'TestPassword1*',
                                          'password2': 'TestPassword1*'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/'))
        self.assertEqual(User.objects.latest('id').username, 'testusername')

    def test_post_fail(self):
        response = self.client.post('/signup/',
                                    data={'username': 'testusernamefalse',
                                          'first_name': 'testfirstname',
                                          'last_name': 'testlastname',
                                          'email': 'test@email.com'})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            User.objects.latest('id').username == 'testusernamefalse')


class SearchViewTest(TestCase):
    def setUp(self):
        self.product1 = Product.objects.create(
            name='Cola',
            brand='Coca',
            nutri_score='e',
            url_off='https://off.fr/cola',
            url_image='https://image-cola.fr',
            nutriments_100g='{glucose_100g: 6}')
        self.product2 = Product.objects.create(
            name='Eau',
            brand='Evian',
            nutri_score='a',
            url_off='https://off.fr/eau',
            url_image='https://image-eau.fr',
            nutriments_100g='{glucose_100g: 6}')
        self.product3 = Product.objects.create(
            name='kinder Maxi',
            brand='Kinder',
            nutri_score='e',
            url_off='https://off.fr/kinder',
            url_image='https://image-kinder.fr',
            nutriments_100g='{glucose_100g: 70}')
        self.category1 = Category.objects.create(name_cat='boisson')
        self.category2 = Category.objects.create(name_cat='snack')
        self.product1.category.add(self.category1)
        self.product2.category.add(self.category1)
        self.product3.category.add(self.category2)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/recherche/')
        self.assertEqual(response.status_code, 200)

    def test_post_show_products_substitutes(self):
        response = self.client.post('/recherche/', data={'search': 'cola'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.product1 in response.context['products'])

    def test_post_dont_show_products_not_substitutes(self):
        response = self.client.post('/recherche/', data={'search': 'cola'})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(self.product3 in response.context['products'])


class PasswordResetViewTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='testuser',
                                                  password='testpassword',
                                                  email='testuser@email.fr')
        self.test_user.save()

    def test_view_send_mail(self):
        self.assertEqual(len(mail.outbox), 0)
        response = self.client.post('/password_reset/',
                                    data={'email': 'testuser@email.fr'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)

    def test_view_not_send_mail(self):
        self.assertEqual(len(mail.outbox), 0)
        response = self.client.post('/password_reset/',
                                    data={'email': 'test@email.fr'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 0)


class ContactViewTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='testuser',
                                                  password='testpassword',
                                                  email='testuser@email.fr')
        self.test_user.save()

    def test_view_send_mail(self):
        self.assertEqual(len(mail.outbox), 0)
        response = self.client.post('/contact/',
                                    data={'name': 'testuser',
                                          'email': 'testuser@email.fr',
                                          'message':
                                              'Impossible de me connecter.'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)

    def test_view_not_send_mail(self):
        self.assertEqual(len(mail.outbox), 0)
        response = self.client.post('/contact/',
                                    data={'name': 'testuser',
                                          'message':
                                              'Impossible de me connecter.'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 0)
