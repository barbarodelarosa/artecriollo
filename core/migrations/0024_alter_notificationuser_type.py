# Generated by Django 4.0.2 on 2022-05-27 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_alter_notificationuser_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationuser',
            name='type',
            field=models.CharField(choices=[('ONE_USER', 'ONE_USER'), ('GROUP_USER', 'GROUP_USER'), ('ALL_USER', 'ALL_USER'), ('ALL_USER_AUTHENTICATED', 'ALL_USER_AUTHENTICATED')], max_length=22),
        ),
    ]
