from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Feature(models.Model):
    feature = models.CharField(max_length=64)

    def __str__(self):
        return f" {self.feature} "

class Product(models.Model):
    product_name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    imege = models.URLField()
    category = models.ForeignKey(Feature, on_delete=models.PROTECT, related_name="category")

    def __str__(self):
        return f"{self.id}: {self.product_name} to {self.category}"

    