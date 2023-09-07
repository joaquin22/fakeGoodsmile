from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

from .choices import UserTypeChoices


class User(AbstractUser):
    email = models.EmailField(verbose_name="Email", max_length=255, unique=True)
    user_type = models.CharField(
        max_length=20,
        choices=UserTypeChoices.choices,
        default=UserTypeChoices.USER,
    )

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Manufacturer(models.Model):
    name = models.CharField(_("Name"), max_length=200)

    class Meta:
        verbose_name = _("Manufacter")
        verbose_name_plural = _("Manufacters")

    def __str__(self):
        return self.name


class Serie(models.Model):
    name = models.CharField(_("Name"), max_length=200)

    class Meta:
        verbose_name = _("Serie")
        verbose_name_plural = _("Series")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    description = models.TextField(_("Description"))
    price = models.IntegerField(_("Price"), default=100)
    manufacturer = models.ForeignKey(
        Manufacturer, verbose_name=_("Manufacturer"), on_delete=models.CASCADE
    )
    serie = models.ForeignKey(Serie, verbose_name=_("Serie"), on_delete=models.CASCADE)
    specifications = models.TextField(_("Specifications"))
    release_date = models.DateField(
        _("Release Date"), auto_now=False, auto_now_add=False
    )

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name=_("Product"),
        related_name="images",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    image = models.ImageField(
        _("Image Product"),
        upload_to="product/",
        height_field=None,
        width_field=None,
        max_length=None,
    )

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")
