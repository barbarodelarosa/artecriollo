# Generated by Django 4.0.2 on 2022-06-02 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_address_map_address_address_map_langitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='map_id',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
