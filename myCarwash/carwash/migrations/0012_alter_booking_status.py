# Generated by Django 5.1.2 on 2024-10-12 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carwash', '0011_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(default='Not yet', max_length=100),
        ),
    ]