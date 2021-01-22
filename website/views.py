from django.shortcuts import render
from django.views import View

from website.models import Product


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


def list_product(request):
    products = Product.objects.all()
    return render(request, 'list_product.html', {"products": products})
