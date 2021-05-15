from django.contrib.auth.models import AbstractUser
from django.db import models


class Category(models.Model):
    """Store a category in the database"""
    name_cat = models.CharField(max_length=255, unique=True)


class Store(models.Model):
    """Store a store in the database"""
    name_store = models.CharField(max_length=255, unique=True)


class Product(models.Model):
    """Store a product in the database"""
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, null=True)
    nutri_score = models.CharField(max_length=2, null=True)
    url_off = models.TextField(null=True)
    url_image = models.TextField(null=True)
    nutriments_100g = models.TextField(null=True)
    category = models.ManyToManyField(Category)
    store = models.ManyToManyField(Store)

    class Meta:
        unique_together = ["name", "brand", "url_off"]


class User(AbstractUser):
    """Store an user in the database"""
    product = models.ManyToManyField(Product, blank=True)
