# Generated by Django 4.2.1 on 2023-06-05 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0002_roominfo_facilities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomfacility',
            name='color',
        ),
        migrations.RemoveField(
            model_name='roomfacility',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='roomfacility',
            name='room',
        ),
    ]