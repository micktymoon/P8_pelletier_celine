from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, TemplateView
from django.contrib.auth import login, get_user_model
from website.models import Product
from website.forms import SignUpForm, SearchForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_prod = form.cleaned_data['search']
            product = Product.objects.all()
            product = product.filter(name__icontains=search_prod)
            return render(request, 'search.html', {'search': search_prod,
                                                   'products': product})
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form})


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


class AccountView(DetailView):
    model = get_user_model()
    template_name = 'account.html'

    def get_object(self, queryset=None):
        return self.request.user



