from django.core import mail
from django.test import override_settings
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import sys
import os
import time

from website.models import User, Product, Category


@override_settings(
    EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
class UserStoryTest(StaticLiveServerTestCase):
    @classmethod
    def setUp(cls):
        super().setUpClass()
        sys.path.append(os.path.abspath('driver/geckodriver'))
        cls.browser = webdriver.Firefox(
            executable_path=os.path.abspath('driver/geckodriver'))
        cls.test_user = User.objects.create_user(username='testuser',
                                                 password='cP93*mR78.',
                                                 email='testuser@email.fr')
        cls.test_user.save()
        cls.product = Product.objects.create(name='Dolce Pizza - Regina',
                                             brand='Dolce Pizza',
                                             nutri_score='e',
                                             url_off='https://off.fr/Regina',
                                             url_image='https://image-regina.'
                                                       'fr',
                                             nutriments_100g='{glucose_100g: '
                                                             '6}')
        cls.product.save()
        cls.cat = Category.objects.create(name_cat='pizza')
        cls.cat.save()
        cls.product.category.add(cls.cat)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_user_story(self):
        self.browser.get('%s%s' % (self.live_server_url, '/'))
        self.assertIn('Pur Beurre', self.browser.title)
        login = self.browser.find_element_by_css_selector('a.fa-sign-in-alt')
        login.click()
        self.assertEqual(
            self.browser.find_element_by_css_selector('h1').text,
            "Connexion")
        user_name = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        user_name.send_keys("testuser")
        time.sleep(1)
        password.send_keys("cP93*mR78.")
        time.sleep(1)
        btn_login = self.browser.find_element_by_class_name('button')
        btn_login.click()
        time.sleep(1)
        self.assertEqual(self.browser.find_element_by_css_selector('h1').text,
                         "Du gras, oui, mais de qualité!")
        account = self.browser.find_element_by_class_name('fa-user')
        account.click()
        time.sleep(1)
        self.assertTrue("Ahoy" in
                        self.browser.find_element_by_css_selector('h1').text)
        search = self.browser.find_element_by_name('search')
        search.send_keys('pizza')
        time.sleep(1)
        btn_search = self.browser.find_element_by_class_name('my-sm-0')
        btn_search.click()
        time.sleep(1)
        self.assertEqual(self.browser.find_element_by_css_selector('h1').text,
                         'Votre recherche')
        first_product = self.browser.find_element_by_class_name(
            'col-sm-12:nth-child(1)')
        self.assertEqual(
            first_product.find_element_by_class_name('card-title').text,
            'Dolce Pizza - Regina')
        time.sleep(1)
        btn_save = first_product.find_element_by_name('save')
        btn_save.click()
        time.sleep(1)
        self.assertEqual(
            self.browser.find_element_by_css_selector('h1').text,
            'Dolce Pizza - Regina')
        btn_carrot = self.browser.find_element_by_xpath(
            '//a[contains(@href, "/mesaliments/")]')
        btn_carrot.click()
        time.sleep(1)
        self.assertEqual(
            self.browser.find_element_by_css_selector('h1').text,
            'Mes aliments')
        btn_logout = self.browser.find_element_by_class_name('fa-sign-out-alt')
        btn_logout.click()
        time.sleep(1)
        self.assertEqual(self.browser.find_element_by_css_selector('h1').text,
                         "Du gras, oui, mais de qualité!")

    def test_change_password(self):
        self.browser.get('%s%s' % (self.live_server_url, '/'))
        self.assertEqual(len(mail.outbox), 0)
        login = self.browser.find_element_by_css_selector('a.fa-sign-in-alt')
        login.click()
        user_name = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        user_name.send_keys("testuser")
        time.sleep(1)
        password.send_keys("cP93*mR78.")
        time.sleep(1)
        btn_login = self.browser.find_element_by_class_name('button')
        btn_login.click()
        time.sleep(1)
        account = self.browser.find_element_by_class_name('fa-user')
        account.click()
        time.sleep(1)
        changepassword = self.browser.find_element_by_id('changepassword')
        changepassword.click()
        email = self.browser.find_element_by_id('id_email')
        email.send_keys('testuser@email.fr')
        time.sleep(1)
        btn_changepassword = self.browser.find_element_by_name('submit')
        btn_changepassword.click()
        self.assertEqual(len(mail.outbox), 1)
        time.sleep(1)
