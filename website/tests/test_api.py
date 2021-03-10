import unittest
from unittest.mock import patch
from website.api import get_word_remove_spaces, search_product


class GetWordRemoveSpacesTest(unittest.TestCase):
    def test_get_word_remove_spaces_works(self):
        text = "Coca, Sprite, Evian"
        self.assertEqual(get_word_remove_spaces(text), ['Coca',
                                                        'Sprite',
                                                        'Evian'])

    def test_get_word_remove_spaces_return_null(self):
        text = None
        self.assertEqual(get_word_remove_spaces(text), 'NULL')


class MockResponse:
    def __init__(self):
        self.status_code = 200
        self.text = '{"products": [{"product_name": "prince",' \
                    '"brands": "prince", "categories": "snacks",' \
                    '"nutriscore_grade": "d", "stores": "Auchan", ' \
                    '"url": "www.off.fr/prince", ' \
                    '"image_small_url": "www.image-prince.fr", ' \
                    '"nutriments": {"glucose_100g": "6"}}]}'

    def json(self):
        return {"products": [
                {"product_name": "prince",
                 "brands": "prince",
                 "categories": "snacks",
                 "nutriscore_grade": "d",
                 "stores": "Auchan",
                 "url": "www.off.fr/prince",
                 "image_small_url": "www.image-prince.fr",
                 "nutriments": {"glucose_100g": "6"}}]}


class SearchProductTest(unittest.TestCase):
    @patch("requests.get", return_value=MockResponse())
    def test_search_product_works(self, mocked):
        result = [{"name": "prince",
                   "brand": "prince",
                   "category": ["snacks"],
                   "nutriscore": "d",
                   "store": ["Auchan"],
                   "url": "www.off.fr/prince",
                   "image": "www.image-prince.fr",
                   "nutriments-100g": {"glucose_100g": "6"}}]
        self.assertEqual(search_product('prince'), result)


if __name__ == '__main__':
    unittest.main()
