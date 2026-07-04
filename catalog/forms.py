from django import forms
from django.forms import inlineformset_factory
from .models import Product, ProductImage
from shop.forms_utils import apply_bootstrap_classes

class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        apply_bootstrap_classes(self)

class ProductForm(BootstrapModelForm):
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
