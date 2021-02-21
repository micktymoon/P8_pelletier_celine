from django.urls import path, include
from django.contrib.auth import views
from website import views as website_views

urlpatterns = [
    path('', website_views.HomeView.as_view(), name="home"),
    path('mesaliments/', website_views.MyProductView.as_view(), name="my_product"),
    path('detail/<int:pk>/', website_views.ProductView.as_view(), name="detail"),
    path('account/', website_views.AccountView.as_view(), name="account"),
    path('signup/', website_views.signup, name="signup"),
    path('login/', views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('recherche/', website_views.search, name='search'),
    path('sauvegarde/<int:product_id>/', website_views.save, name="save"),
]
