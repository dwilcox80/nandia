from django.contrib import admin
from .models import CrustType, Pizza, PizzaSize, SauceAmount, SauceType, Topping


admin.site.register(CrustType)
admin.site.register(Pizza)
admin.site.register(PizzaSize)
admin.site.register(SauceAmount)
admin.site.register(SauceType)
admin.site.register(Topping)
