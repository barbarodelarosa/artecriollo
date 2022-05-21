# Generated by Django 4.0.2 on 2022-05-13 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_notificationuser_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationuser',
            name='type',
            field=models.CharField(choices=[('ALL_USER', 'ALL_USER'), ('GROUP_USER', 'GROUP_USER'), ('ALL_USER_AUTHENTICATED', 'ALL_USER_AUTHENTICATED'), ('ONE_USER', 'ONE_USER')], max_length=22),
        ),
    ]