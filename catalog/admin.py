from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Product, ProductImage


class ProductImageInline(admin.TabularInline):
    """Встраиваемое отображение дополнительных изображений на странице товара."""

    model = ProductImage
    extra = 1  # количество пустых форм для добавления
    fields = ("image", "position", "is_active")
    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height:50px;">')
        return "-"

    preview.short_description = "Предпросмотр"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "parent", "is_active", "position", "created_at")
    list_filter = ("is_active", "parent")
    search_fields = ("name", "slug", "description")
    prepopulated_fields = {"slug": ("name",)}
    raw_id_fields = ("parent",)
    list_editable = ("position", "is_active")
    ordering = ("position", "name")
    fieldsets = (
        (None, {"fields": ("name", "slug", "description", "image")}),
        ("Иерархия", {"fields": ("parent",)}),
        ("Настройки отображения", {"fields": ("is_active", "position")}),
        ("Даты", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )
    readonly_fields = ("created_at", "updated_at")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price",
        "compare_price",
        "quantity",
        "is_active",
    )
    # list_display = ('name', 'category', 'price', 'compare_price', 'quantity', 'is_active', 'is_stock_display')
    list_filter = ("category", "is_active", "quantity")
    search_fields = ("name", "slug", "description")
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ("price", "compare_price", "quantity", "is_active")
    ordering = ("position", "name")
    # raw_id_fields = ("category",)
    autocomplete_fields = ('category',)
    inlines = [ProductImageInline]
    fieldsets = (
        (None, {"fields": ("name", "slug", "description", "category", "image")}),
        ("Цены и наличие", {"fields": ("price", "compare_price", "quantity")}),
        ("Настройки отображения", {"fields": ("is_active", "position")}),
        ("Даты", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )
    readonly_fields = ("created_at", "updated_at")

    @admin.display(boolean=True, description="В наличии")
    def in_stock_display(self, obj):
        return obj.quantity > 0


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "position", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("product__name",)
    raw_id_fields = ("product",)
