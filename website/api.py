#!/usr/bin/python3
# -*-coding: utf8 -*-

import json
import requests


def get_word_remove_spaces(text):
    """
    Retrieves the words of a text in a list and removes spaces before
     and after each word.

    Parameters:
        text : str
            The text whose words we want to recover.

    Returns:
        list
            The list of text words.
    """
    list_words = text.split(",")
    list_without_spaces = []
    for word in list_words:
        word = word.strip()
        list_without_spaces.append(word)
    return list_without_spaces


def search_product(name_product):
    """
    Search a product in OpenFoodFact API and return a list of products
     found.

    Complete the link with the name of the product we are looking for,
     search for the corresponding products and return a list of products
     found.

    Parameters:
        name_product: str
            The name of the product we're looking for.

    Returns:
        list
            A list of products found by the API.
    """
    api_search_terms = "https://fr.openfoodfacts.org/cgi/search.pl?" \
                       "action=process&json=1&search_terms="
    final_http = api_search_terms + name_product
    response = requests.get(final_http)
    response_text = json.loads(response.text)
    i = 0
    product_list = []
    while i < len(response_text):
        try:
            path = response_text["products"][i]
            final_product = {"name": path["product_name"],
                             "brand": path.get("brands", None),
                             "category": get_word_remove_spaces(
                                 path.get("categories", None)),
                             "nutriscore": path.get(
                                 "nutriscore_grade", None),
                             "store": get_word_remove_spaces(
                                 path.get("stores", None)),
                             "url": path.get("url", None),
                             "image": path.get("image_small_url", None),
                             }
            nutriment_100g = {}
            nutriments = path.get('nutriments', None)
            for nutriment in nutriments:
                if nutriment.endswith("_100g"):
                    nutriment_100g[nutriment] = path["nutriments"][nutriment]

            final_product["nutriments-100g"] = nutriment_100g

            if final_product["url"] is None:
                start = "https://fr.openfoodfacts.org/produit/"
                id_prod = path["code"]
                final_product["url"] = start + id_prod
            product_list.append(final_product)
            i += 1
        except IndexError:
            i += 1
            pass
    return product_list

print(search_product('prince'))

