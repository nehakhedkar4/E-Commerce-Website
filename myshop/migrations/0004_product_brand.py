# Generated by Django 4.1.4 on 2022-12-22 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0003_alter_product_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
