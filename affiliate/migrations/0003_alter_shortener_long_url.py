# Generated by Django 4.0.2 on 2022-03-29 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affiliate', '0002_shortener_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortener',
            name='long_url',
            field=models.SlugField(),
        ),
    ]
