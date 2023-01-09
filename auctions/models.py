from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.user}"
    

class Feature(models.Model):
    feature = models.CharField(max_length=64)

    def __str__(self):
        return f" {self.feature} "


class Product(models.Model):
    product_name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    imege = models.URLField()
    category = models.ForeignKey(Feature, on_delete=models.PROTECT, related_name="category")
    marketeer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="marketeer")

    def __str__(self):
        return f"{self.id}: {self.product_name}, {self.category}, {self.marketeer}"




    