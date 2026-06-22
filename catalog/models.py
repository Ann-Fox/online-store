from django.db import models
# from django.urls import reverse
# from django.utils.text import slugify


class Category(models.Model):
    """
    Категория товаров с поддержкой древовидной структуры.
    """

    name = models.CharField(max_length=200, verbose_name="Название категории")
    slug = models.SlugField(unique=True, verbose_name="Слаг (URL)")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="category/", blank=True, null=True, verbose_name="Изображение"
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="children",
        verbose_name="Родительская категория",
    )
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    position = models.PositiveIntegerField(default=0, verbose_name="Порядок сортировки")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создана")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлена")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("position", "name")  # сортировка по порядку, затем по имени
        # indexes = [
        #     models.Index(fields=["slug"]),
        #     models.Index(fields=["parent"]),
        # ]

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("catalog:category_detail", kwargs={"slug": self.slug})

    # def save(self, *args, **kwargs):
    #     # Если slug не задан, генерируем из названия
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)

    # # Дополнительно: метод для получения полного пути (от корня до текущей)
    # def get_full_path(self):
    #     """
    #     Возвращает список названий категорий от корня до текущей (для хлебных крошек).
    #     """
    #     categories = []
    #     category = self
    #     while category:
    #         categories.append(category.name)
    #         category = category.parent
    #     return reversed(categories)
