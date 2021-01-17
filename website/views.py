from django.shortcuts import render

from website.models import Product


def list_product(request):
    products = Product.objects.all()
    return render(request, 'list_product.html', {"products": products})
