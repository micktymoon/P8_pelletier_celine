from django.core.management import BaseCommand
from website.api import search_product
from website.models import Product, Category, Store


class Command(BaseCommand):
    help = 'File the database with some products.'

    def handle(self, *args, **options):
        list_name = ["eau", "jus de pomme", "sprite", "prince", "kinder",
                     "pizza regina", "pizza 4 fromages", "magnum amande",
                     "glace vanille", "camembert", "sainte maure",
                     "pulco", "haricot", "petit pois"]

        for name in list_name:
            list_products = search_product(name)
            for product in list_products:
                objects = Product(name=product['name'],
                                  brand=product['brand'],
                                  nutri_score=product['nutriscore'],
                                  url_off=product['url'],
                                  url_image=product['image'],
                                  nutriments_100g=product['nutriments-100g']
                                  )

                categories = product['category']
                for category in categories:
                    cat = Category(name_cat=category)
                    objects.category.add(cat)

                stores = product['store']
                for store in stores:
                    sto = Store(name_store=store)
                    objects.store.add(sto)
