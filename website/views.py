from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView

from website.models import Product


class HomeView(TemplateView):
    template_name = 'home.html'


class MyProductView(ListView):
    model = Product
    paginate_by = 20
    template_name = 'list_product.html'
    context_object_name = "products"


class ProductView(DetailView):
    model = Product
    template_name = 'detail.html'
    slug_field = 'id'


class ResultsView(View):
    def get(self, request):
        pass
