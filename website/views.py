from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, TemplateView
from django.contrib.auth import login, get_user_model
from django.db.models import Q
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
            product = Product.objects.\
                filter(name__icontains=search_prod).first()
            if product is not None:
                subsitutes = Product.objects.filter(
                    Q(nutri_score__lte=product.nutri_score),
                    Q(category__in=product.category.all())).\
                    distinct('name', 'nutri_score').order_by('nutri_score')

                return render(request, 'search.html', {'search': search_prod,
                                                       'products': subsitutes,
                                                       'form': form})
            else:
                render(request, 'search.html', {'search': search_prod,
                                                'products': product,
                                                'form': form})
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form})


def save(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_authenticated:
        user = request.user
        user.product.add(product)
        return redirect('detail', pk=product_id)
    else:
        return redirect('signup')


class HomeView(TemplateView):
    template_name = 'home.html'


class MyProductView(ListView):
    paginate_by = 20
    template_name = 'list_product.html'
    context_object_name = "products"

    def get_queryset(self):
        user = self.request.user
        products = Product.objects.filter(pk__in=user.product.all())
        return products


class ProductView(DetailView):
    model = Product
    template_name = 'detail.html'


class AccountView(DetailView):
    model = get_user_model()
    template_name = 'account.html'

    def get_object(self, queryset=None):
        return self.request.user


class LegalNoticeView(TemplateView):
    template_name = 'legal_notice.html'
