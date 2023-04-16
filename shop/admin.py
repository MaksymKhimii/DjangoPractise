from django.contrib import admin
from .models import User, Product, Basket, BasketProducts, Order, OrderProducts, UserDetails

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(BasketProducts)
admin.site.register(Order)
admin.site.register(OrderProducts)
admin.site.register(UserDetails)