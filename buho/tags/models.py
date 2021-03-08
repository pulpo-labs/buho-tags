from buho.helpers import mixins
from django.contrib.gis.db import models


class TagCategory(models.TextChoices):
    SERVICES = 'SERVICES', 'SERVICES'
    PAYMENT_METHODS = 'PAYMENT_METHODS', 'PAYMENT_METHODS'
    FOOD_TYPE = 'FOOD_TYPE', 'FOOD_TYPE'
    INFRASTRUCTURE = 'INFRASTRUCTURE', 'INFRASTRUCTURE'


class Tag(
    mixins.SoftDeleteMixin,
    mixins.TimestampsMixin
):
    category = models.CharField(max_length=50, choices=TagCategory.choices)
    text = models.CharField(max_length=255)

    class Meta:
        abstract = True
