# Generated by Django 4.0.2 on 2022-03-13 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_socialred_icon_alter_socialred_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteinfo',
            name='icon',
            field=models.ImageField(default='/static/media/images/logo.png', upload_to='image/icon'),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='logo',
            field=models.ImageField(default='/static/media/images/logo.png', upload_to='image/logo'),
        ),
    ]
