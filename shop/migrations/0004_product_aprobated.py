# Generated by Django 4.0.2 on 2022-03-24 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_merchant_aprobated'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='aprobated',
            field=models.BooleanField(default=False),
        ),
    ]
