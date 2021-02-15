from django.contrib.auth.models import AbstractUser
from django.db import models


class Category(models.Model):
    name_cat = models.CharField(max_length=255, unique=True)


class Store(models.Model):
    name_store = models.CharField(max_length=255, unique=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, null=True)
    nutri_score = models.CharField(max_length=2)
    url_off = models.TextField(null=True)
    url_image = models.TextField(null=True)
    nutriments_100g = models.TextField(null=True)
    category = models.ManyToManyField(Category)
    store = models.ManyToManyField(Store)

    class Meta:
        unique_together = ["name", "brand", "url_off"]


class User(AbstractUser):
    product = models.ManyToManyField(Product, blank=True)







