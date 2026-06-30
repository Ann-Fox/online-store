from django import forms
from django.forms import inlineformset_factory
from .models import Product, ProductImage


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "name",
            "slug",
            "description",
            "category",
            "price",
            "is_active",
            "quantity",
            "image",
        )


ProductImageFormSet = inlineformset_factory(
    Product,
    ProductImage,
    fields=("image", "position", "is_active"),
    extra=4,  # количество пустых форм для добавления
    can_delete=True,  # позволит удалять изображения
)
