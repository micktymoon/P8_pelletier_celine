from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from website.models import Product


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('HomeView')
    else:
        form = UserCreationForm
    return render(request, 'signup.html', {'form': form})


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
