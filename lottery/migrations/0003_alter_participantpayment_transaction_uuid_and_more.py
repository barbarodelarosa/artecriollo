# Generated by Django 4.0.2 on 2022-05-21 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0002_alter_participant_lottery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantpayment',
            name='transaction_uuid',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='participantpayment',
            name='user_uuid',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
