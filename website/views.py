from django.shortcuts import render
from django.views import View

from website.models import Product


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


class MyProductView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'list_product.html', {"products": products})


class ProductView(View):
    def get(self, request, id_product):
        product = Product.objects.get(pk=id_product)
        return render(request, 'detail.html', {"product": product})


class ResultsView(View):
    def get(self, request):
        pass
