# Generated by Django 4.2.1 on 2023-06-05 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roominfo',
            name='facilities',
            field=models.ManyToManyField(blank=True, to='booking_app.roomfacility'),
        ),
    ]