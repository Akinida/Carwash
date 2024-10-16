# Generated by Django 5.1.2 on 2024-10-09 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carwash', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='service',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='booking',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]