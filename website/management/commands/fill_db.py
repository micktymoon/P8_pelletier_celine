from django.core.management import BaseCommand
from django.db.utils import IntegrityError
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
                obj, created = Product.objects.get_or_create(
                    name=product['name'],
                    brand=product['brand'],
                    url_off=product['url'],
                    defaults={
                        "url_image": product['image'],
                        "nutriments_100g": product['nutriments-100g']
                    },
                )

                categories = product['category']
                for category in categories:
                    cat, cat_created = Category.objects.get_or_create(name_cat=category)
                    obj.category.add(cat)

                stores = product['store']
                for store in stores:
                    sto, sto_created = Store.objects.get_or_create(name_store=store)
                    obj.store.add(sto)
