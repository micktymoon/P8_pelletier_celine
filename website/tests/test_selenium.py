# from selenium import webdriver
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# import sys
# import os
# import time
#
#
# class UserStoryTest(StaticLiveServerTestCase):
#     @classmethod
#     def setUp(cls):
#         sys.path.append(os.path.abspath('driver/geckodriver'))
#         cls.browser = webdriver.Firefox(
#             executable_path=os.path.abspath('driver/geckodriver'))
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.browser.quit()
#         super().tearDownClass()
#
#     def test_user_story(self):
#         self.browser.get("https://celine-bienmanger.herokuapp.com/")
#         self.assertIn('Pur Beurre', self.browser.title)
#         login = self.browser.find_element_by_css_selector('a.fa-sign-in-alt')
#         login.click()
#         self.assertEqual(
#             self.browser.find_element_by_css_selector('h1').text,
#             "Connexion")
#         user_name = self.browser.find_element_by_id('id_username')
#         password = self.browser.find_element_by_id('id_password')
#         user_name.send_keys("test_username")
#         time.sleep(1)
#         password.send_keys("cP93*mR78.")
#         time.sleep(1)
#         btn_login = self.browser.find_element_by_class_name('button')
#         btn_login.click()
#         time.sleep(1)
#         self.assertEqual(self.browser.find_element_by_css_selector('h1').text,
#                          "Du gras, oui, mais de qualité!")
#         account = self.browser.find_element_by_class_name('fa-user')
#         account.click()
#         time.sleep(3)
#         self.assertTrue("Ahoy" in
#                         self.browser.find_element_by_css_selector('h1').text)
#         search = self.browser.find_element_by_name('search')
#         search.send_keys('pizza')
#         time.sleep(1)
#         btn_search = self.browser.find_element_by_class_name('my-sm-0')
#         btn_search.click()
#         time.sleep(1)
#         self.assertEqual(self.browser.find_element_by_css_selector('h1').text,
#                          'Votre recherche')
#         first_product = self.browser.find_element_by_class_name(
#             'col-sm-12:nth-child(1)')
#         self.assertEqual(
#             first_product.find_element_by_class_name('card-title').text,
#             'Dolce Pizza - Regina')
#         btn_save = first_product.find_element_by_link_text('Sauvegarder')
#         btn_save.click()
#         time.sleep(3)
#         self.assertEqual(
#             self.browser.find_element_by_css_selector('h1').text,
#             'Dolce Pizza - Regina')
#         btn_carrot = self.browser.find_element_by_xpath(
#             '//a[contains(@href, "/mesaliments/")]')
#         btn_carrot.click()
#         time.sleep(1)
#         self.assertEqual(
#             self.browser.find_element_by_css_selector('h1').text,
#             'Mes aliments')
#         btn_logout = self.browser.find_element_by_class_name('fa-sign-out-alt')
#         btn_logout.click()
#         time.sleep(3)
#         self.assertEqual(self.browser.find_element_by_css_selector('h1').text,
#                          "Du gras, oui, mais de qualité!")
#
