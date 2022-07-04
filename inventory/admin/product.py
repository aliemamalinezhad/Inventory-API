from django.contrib import admin



class InventoryAdmin(admin.ModelAdmin):
    list_display = ("product", "store_price")
 