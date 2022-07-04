from django.db import models
from django.utils.translation import gettext_lazy as _
from inventory.models.product import ProductInventory

class Stock(models.Model):
    product_inventory = models.OneToOneField(
        ProductInventory,
        related_name="product_inventory",
        on_delete=models.PROTECT,
    )
    last_checked = models.DateTimeField(
        null=True,
        blank=True,
    )
    units = models.IntegerField(
        default=0,
    )
    units_sold = models.IntegerField(
        default=0,
    )

