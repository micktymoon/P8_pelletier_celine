from django.contrib.auth.models import AbstractUser
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, null=True)
    nutri_score = models.CharField(max_length=2, null=True)
    ingredient = models.TextField(null=True)
    url_off = models.TextField(null=True)
    url_image = models.TextField(null=True)
    prix = models.DecimalField(max_digits=5, decimal_places=2)
