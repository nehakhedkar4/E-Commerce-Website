# Generated by Django 3.2.12 on 2022-12-27 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0006_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='customer',
        ),
    ]