# Generated by Django 5.1.2 on 2024-10-09 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carwash', '0004_booking_vehicle_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='no_phone',
            field=models.CharField(max_length=100, null=True),
        ),
    ]