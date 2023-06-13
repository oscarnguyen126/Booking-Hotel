from django.db import models
from django.contrib.auth.models import AbstractUser, _


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(_("username"), max_length=200, unique=True)
    password = models.CharField(_("password"))
    is_staff = models.BooleanField(
        "staff status",
        default=False,
    )
    is_active = models.BooleanField(
        "active",
        default=True,
    )

    def __str__(self):
        return self.email + self.password
