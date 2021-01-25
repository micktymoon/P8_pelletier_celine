from django.urls import path, include

from website import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('mesaliments/', views.MyProductView.as_view(), name="my_product"),
    path('resultats/', views.ResultsView.as_view(), name="results"),
    path('detail/<int:id_product>/', views.ProductView.as_view(), name="detail"),
    path('accounts/', include('django.contrib.auth.urls')),
]
