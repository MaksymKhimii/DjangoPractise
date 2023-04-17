from django.db import models


class User(models.Model):
    id = models.IntegerField
    username = models.CharField('username', max_length=225)
    password = models.CharField('password', max_length=225)

    def __str__(self):
        return self.username


class Product(models.Model):
    title = models.CharField('title', max_length=255)
    price = models.FloatField(verbose_name='price', null=True)
    img = models.TextField(verbose_name='img', null=True)


class Basket(models.Model):
    id = models.IntegerField
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class BasketProducts(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    countOfProducts = models.PositiveIntegerField(default=1)


class Order(models.Model):
    id = models.IntegerField
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField('status', max_length=255)


class OrderProducts(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    countOfProducts = models.PositiveIntegerField(default=1)


class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField('email', max_length=255)
    phone = models.CharField('phone', max_length=10)
