from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from inventory.models.product import ProductInventory


class Media(models.Model):
    product_inventory = models.ForeignKey(
        ProductInventory,
        on_delete=models.PROTECT,
        related_name="media",
    )
    img_url = models.ImageField()
    alt_text = models.CharField(
        max_length=255,
    )
    is_feature = models.BooleanField(
        default=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
