from django.db import models


class Customer(models.Model):
    id = models.IntegerField
    username = models.CharField(verbose_name="ім'я", max_length=225)
    password = models.CharField(verbose_name='пароль', max_length=225)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Клієнт'
        verbose_name_plural = 'Клієнти'


class Product(models.Model):
    title = models.CharField(verbose_name='назва товару', max_length=255)
    price = models.FloatField(verbose_name='ціна', null=True)
    img = models.TextField(verbose_name='Посилання на зображення', null=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'


class Basket(models.Model):
    id = models.IntegerField
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='клієнт')

    class Meta:
        verbose_name = 'Кошик'
        verbose_name_plural = 'Кошики'


class BasketProducts(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, verbose_name='кошик')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='товар')
    countOfProducts = models.PositiveIntegerField(default=1, verbose_name='кількість товару')

    class Meta:
        verbose_name = 'Товари кошику'
        verbose_name_plural = 'Товари кошиків'


class Order(models.Model):
    id = models.IntegerField
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='клієнт')
    status = models.CharField(max_length=255, verbose_name='статус')

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'


class OrderProducts(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='замовлення')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='товар')
    countOfProducts = models.PositiveIntegerField(default=1, verbose_name='кількість товару')

    class Meta:
        verbose_name = 'Продукти замовлення'
        verbose_name_plural = 'Продукти замовлень'


class CustomerDetails(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='клієнт')
    email = models.CharField(max_length=255, verbose_name='електронна пошта')
    phone = models.CharField(max_length=10, verbose_name='номер телефону')

    class Meta:
        verbose_name = 'Деталі клієнта'
        verbose_name_plural = 'Деталі клієнтів'
