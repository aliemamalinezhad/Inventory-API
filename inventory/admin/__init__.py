from django.contrib import admin

from inventory.admin.product import InventoryAdmin
from inventory.models.product import (
    Product as ProductModel,
    ProductInventory as ProductInventoryModel

)
from inventory.models.category import (
    Category as CategoryModel
)

admin.site.register(ProductModel)
admin.site.register(CategoryModel)
admin.site.register(ProductInventoryModel,InventoryAdmin)