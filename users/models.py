from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_accounts = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_reception = models.BooleanField(default=False)
    is_designer = models.BooleanField(default=False)
    is_cutter = models.BooleanField(default=False)
