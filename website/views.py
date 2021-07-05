from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, TemplateView
from django.contrib.auth import login, get_user_model
from django.db.models import Q
from website.models import Product
from website.forms import SignUpForm, SearchForm, ContactForm
from django.http import HttpResponseNotAllowed


def signup(request):
    """A view that displays the new account registration form."""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def contact(request):
    """A view that sends a message to the contact of the website"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email_user = form.cleaned_data['email']
            send_mail('Problème avec le site',
                      f'{name}\n{email_user}\n{message}',
                      email_user,
                      ['micktymoon@gmail.com'])
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def search(request):
    """A view that displays the product search."""
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
    """A view that links a product to a user and redirects
    to the detail page of the saved product.
    If the user is not logged in, redirects to the login page."""
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        if request.user.is_authenticated:
            user = request.user
            user.product.add(product)
            return redirect('detail', pk=product.id)
        else:
            return redirect('login')
    else:
        return HttpResponseNotAllowed('Bad request method')


class HomeView(TemplateView):
    """A view that displays the home page."""
    template_name = 'home.html'


class MyProductView(ListView):
    """A view that displays the products linked to the logged in user."""
    paginate_by = 20
    template_name = 'list_product.html'
    context_object_name = "products"

    def get_queryset(self):
        user = self.request.user
        products = Product.objects.filter(pk__in=user.product.all())
        return products


class ProductView(DetailView):
    """A view that displays the details of a product."""
    model = Product
    template_name = 'detail.html'


class AccountView(DetailView):
    """A view that displays the details of a user account."""
    model = get_user_model()
    template_name = 'account.html'

    def get_object(self, queryset=None):
        return self.request.user


class LegalNoticeView(TemplateView):
    """A view that displays the legal notices of the site."""
    template_name = 'legal_notice.html'


def errortestview(request):
    raise Exception('Erreur Test pour Sentry')
