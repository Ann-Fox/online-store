from catalog.models import Product, ProductImage

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class ProductSerializer(ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        # fields = '__all__'
        fields = (
            "id",
            "name",
            "slug",
            "description",
            "price",
            "image",
            "is_active",
            "position",
            "category",
            "category_name",
        )
        # exclude = ["quantity"]
        model = Product


class ProductImageSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ProductImage
