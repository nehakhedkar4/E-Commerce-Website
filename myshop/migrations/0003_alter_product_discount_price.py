# Generated by Django 4.1.4 on 2022-12-22 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0002_product_discount_price_alter_customer_pincode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.IntegerField(default=0),
        ),
    ]