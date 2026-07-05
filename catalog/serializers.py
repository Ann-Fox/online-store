from catalog.models import Product, ProductImage

from rest_framework.serializers import ModelSerializer


class ProductSerializer(ModelSerializer):
    class Meta:
        # fields = '__all__'
        exclude = ["quantity"]
        model = Product


class ProductImageSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ProductImage
