from buho.helpers import mixins
from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _


class TagCategory(models.TextChoices):
    SERVICES = 'SERVICES', _('Servicios')
    PAYMENT_METHODS = 'PAYMENT_METHODS', _('Métodos de Pago')
    FOOD_TYPE = 'FOOD_TYPE', _('Tipo de comida')
    INFRASTRUCTURE = 'INFRASTRUCTURE', _('Instalaciones')


class Tag(
    mixins.SoftDeleteMixin,
    mixins.TimestampsMixin
):
    category = models.CharField(choices=TagCategory.choices)
    text = models.CharField(max_length=255)

    class Meta:
        abstract = True
