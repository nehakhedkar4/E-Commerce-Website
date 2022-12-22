# Generated by Django 4.1.4 on 2022-12-22 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0005_rename_price_product_selling_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('EL', 'Electronics'), ('M', 'Mobiles'), ('F', 'Fashion'), ('H', 'Home'), ('T', 'Toys'), ('TD', 'Today deals')], max_length=30),
        ),
    ]
