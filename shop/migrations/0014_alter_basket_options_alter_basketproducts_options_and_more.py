# Generated by Django 4.1.7 on 2023-05-04 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_alter_customer_password_alter_customer_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'verbose_name': 'Кошик'},
        ),
        migrations.AlterModelOptions(
            name='basketproducts',
            options={'verbose_name': 'Товари кошику'},
        ),
        migrations.AlterModelOptions(
            name='customerdetails',
            options={'verbose_name': 'Деталі клієнта'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Замовлення', 'verbose_name_plural': 'Замовлення'},
        ),
        migrations.AlterModelOptions(
            name='orderproducts',
            options={'verbose_name': 'Продукти замовлення'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товари'},
        ),
        migrations.AlterField(
            model_name='basket',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customer', verbose_name='клієнт'),
        ),
        migrations.AlterField(
            model_name='basketproducts',
            name='basket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.basket', verbose_name='кошик'),
        ),
        migrations.AlterField(
            model_name='basketproducts',
            name='countOfProducts',
            field=models.PositiveIntegerField(default=1, verbose_name='кількість товару'),
        ),
        migrations.AlterField(
            model_name='basketproducts',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='товар'),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customer', verbose_name='клієнт'),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='email',
            field=models.CharField(max_length=255, verbose_name='електронна пошта'),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='phone',
            field=models.CharField(max_length=10, verbose_name='номер телефону'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customer', verbose_name='клієнт'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(max_length=255, verbose_name='статус'),
        ),
        migrations.AlterField(
            model_name='orderproducts',
            name='countOfProducts',
            field=models.PositiveIntegerField(default=1, verbose_name='кількість товару'),
        ),
        migrations.AlterField(
            model_name='orderproducts',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.order', verbose_name='замовлення'),
        ),
        migrations.AlterField(
            model_name='orderproducts',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='товар'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.TextField(null=True, verbose_name='зображення'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True, verbose_name='ціна'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=255, verbose_name='назва товару'),
        ),
    ]
