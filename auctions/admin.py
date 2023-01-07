from django.contrib import admin
from .models import User, Feature, Product

# Реєструємо ваші моделі.
admin.site.register(User)
admin.site.register(Feature)
admin.site.register(Product)