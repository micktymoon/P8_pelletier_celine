from django.urls import path, include

from website import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('mesaliments/', views.MyProductView.as_view(), name="my_product"),
    path('detail/<slug:slug>/', views.ProductView.as_view(), name="detail"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
]
