# Generated by Django 4.2.2 on 2023-06-13 09:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_user_email_alter_user_password_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=200, verbose_name="password"),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(
                max_length=200, unique=True, verbose_name="username"
            ),
        ),
    ]