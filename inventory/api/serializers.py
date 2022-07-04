from pyexpat import model
from rest_framework import serializers

from inventory.models.product import (
    Product as ProductModel,
    ProductInventory as ProductInventoryModel
) 
from inventory.models.category import (
    Category as CategoryModel
)
from inventory.models.brand import (
    Brand as BrandModel
)




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ["name", "slug", "is_active"]
        read_only = True
    

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = ["name", "web_id"]
        read_only = True
        editable = True


    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['category'] = CategorySerializer(instance.category).data
        return response

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields = ["name"]
        read_only = True



class ProductInventorySearchSerializer(serializers.ModelSerializer):

    product = ProductSerializer(many=False, read_only=True)
    brand = BrandSerializer(many=False, read_only=True)

    class Meta:
        model = ProductInventoryModel
        fields = [
            "id",
            "sku",
            "store_price",
            "is_default",
            "product",
            "brand",
        ]

