# Generated by Django 3.2.13 on 2022-06-17 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0006_alter_lottery_price_lottery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lottery',
            name='related_lottery',
            field=models.ManyToManyField(blank=True, related_name='_lottery_lottery_related_lottery_+', to='lottery.Lottery'),
        ),
    ]