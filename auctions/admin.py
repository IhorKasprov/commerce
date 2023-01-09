from django.contrib import admin
from .models import User, Feature, Product, Profile, Auction


# Реєструємо ваші моделі.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'firstname', 'lastname']

admin.site.register(User)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Feature)
admin.site.register(Product)
admin.site.register(Auction)