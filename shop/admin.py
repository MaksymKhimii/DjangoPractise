from django.contrib import admin
from .models import Customer, Product, Basket, BasketProducts, Order, OrderProducts, CustomerDetails


class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password')
    list_filter = ('id', 'username')
    search_fields = ('id', 'username', 'password')


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'img')
    list_filter = ('title', 'price')
    search_fields = ('title', 'price', 'img')
    list_display_links = ('title', 'price', 'img')


class BasketModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer')
    list_filter = ('id', 'customer')
    search_fields = ('id', 'customer')


class BasketProductsModelAdmin(admin.ModelAdmin):
    def basket_id(self):
        return self.basket.id

    def basket_user(self):
        return self.basket.customer

    def product_title(self):
        return self.product.title

    list_display = (basket_id, basket_user, product_title, 'countOfProducts')
    list_filter = ('basket__id', 'basket__customer', 'product__title', 'countOfProducts')
    search_fields = ('basket_id', 'product_title', 'countOfProducts')
    list_display_links = (basket_id, product_title, 'countOfProducts')


class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status')
    list_filter = ('id', 'customer', 'status')
    search_fields = ('id', 'customer', 'status')


class OrderProductsModelAdmin(admin.ModelAdmin):
    def order_user(self):
        return self.order.customer

    def order_id(self):
        return self.order.id

    def product_title(self):
        return self.product.title

    list_display = (order_id, order_user, product_title, 'countOfProducts')
    list_filter = ('order__id', 'order__customer', 'product__title', 'countOfProducts')
    search_fields = (order_id, order_user, product_title)
    list_display_links = (order_id, product_title, 'countOfProducts')


class CustomerDetailsModelAdmin(admin.ModelAdmin):
    def customer_username(self):
        return self.customer.username

    def customer_id(self):
        return self.customer.id

    list_display = (customer_id, customer_username, 'email', 'phone')
    list_filter = ('customer__id', 'customer__username', 'email', 'phone')
    search_fields = ('customer__id', 'customer__username', 'email', 'phone')
    list_display_links = (customer_id, 'email', 'phone')


admin.site.register(Customer, CustomerModelAdmin)
admin.site.register(Product, ProductModelAdmin)
admin.site.register(Basket, BasketModelAdmin)
admin.site.register(BasketProducts, BasketProductsModelAdmin)
admin.site.register(Order, OrderModelAdmin)
admin.site.register(OrderProducts, OrderProductsModelAdmin)
admin.site.register(CustomerDetails, CustomerDetailsModelAdmin)
