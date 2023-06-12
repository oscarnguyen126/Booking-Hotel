from django.db import models
from django.contrib.auth.models import AbstractUser, _


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), blank=True)
    password = models.CharField(_("password"), max_length=20)
    is_staff = models.BooleanField(
        "staff status",
        default=False,
    )
    is_active = models.BooleanField(
        "active",
        default=True,
    )

    def __str__(self):
        return self.email
