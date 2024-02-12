from django.contrib import admin
from .models import Vegetable, Offer, Fruit


class FruitAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class VegetableAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(Fruit, FruitAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Vegetable, VegetableAdmin)
