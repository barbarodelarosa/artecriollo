# Generated by Django 4.0.2 on 2022-05-01 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_notificationuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationuser',
            name='type',
            field=models.CharField(choices=[('ALL_USER', 'ALL_USER'), ('GROUP_USER', 'GROUP_USER'), ('ONE_USER', 'ONE_USER'), ('ALL_USER_AUTHENTICATED', 'ALL_USER_AUTHENTICATED')], default='ALL_USER', max_length=22),
            preserve_default=False,
        ),
    ]
