from django.db import models


class UserTypeChoices(models.TextChoices):
    ADMIN = "ADMIN", "ADMIN"
    USER = "USER", "USER"
