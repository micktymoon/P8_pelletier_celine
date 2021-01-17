from django.urls import path

from website import views

urlpatterns = [
    path('', views.list_product, name="list_product"),
]