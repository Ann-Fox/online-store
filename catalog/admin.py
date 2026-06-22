from django.contrib import admin
from .models import Category


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
