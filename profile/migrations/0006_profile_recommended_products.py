# Generated by Django 4.0.2 on 2022-03-28 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_aprobated'),
        ('profile', '0005_affiliateapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='recommended_products',
            field=models.ManyToManyField(blank=True, to='shop.Order'),
        ),
    ]
