# Generated by Django 4.0.2 on 2022-04-03 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0005_auction_purchused_auction_purchused_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
