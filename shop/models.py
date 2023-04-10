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
