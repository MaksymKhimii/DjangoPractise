# Generated by Django 4.1.7 on 2023-04-10 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(null=True, verbose_name='price'),
        ),
    ]
