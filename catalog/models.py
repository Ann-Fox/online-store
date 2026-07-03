from django.db import models
from django.urls import reverse
from django.utils.text import slugify


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


class Product(models.Model):
    """
    Модель товара интернет-магазина.
    """

    # Основные поля
    name = models.CharField(max_length=255, verbose_name="Название товара")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Слаг (URL)")
    description = models.TextField(blank=True, verbose_name="Описание")
    category = models.ForeignKey(
        "catalog.Category",
        verbose_name="Категория",
        on_delete=models.CASCADE,
        related_name="products",
    )

    # Цена и скидки
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    compare_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Старая цена (для скидки)",
    )

    # Количество на складе
    quantity = models.PositiveIntegerField(default=0, verbose_name="Остаток")

    # Изображения (главное)
    image = models.ImageField(
        upload_to="products/", blank=True, null=True, verbose_name="Главное изображение"
    )

    # Активность и сортировка
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    position = models.PositiveIntegerField(default=True, verbose_name="Порядок")

    # Даты
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ("position", "name")
        # indexes = [
        #     models.Index(fields=['slug']),
        #     models.Index(fields=['category', 'is_active']),
        # ]

    def __str__(self):
        return self.name

    # ссылка на страницу товара
    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})

    # переопределён для автоматической генерации слага
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


# возвращает цену со скидкой, если есть
# @property
# def discounted_price(self):
#     """Возвращает цену со скидкой, если compare_price задана."""
#     if self.compare_price and self.compare_price > self.price:
#         return self.price
#     return None

# возвращает True, если остаток > 0
# @property
# def in_stock(self):
#     return self.quantity > 0

# проверяет наличие скидки
# @property
# def has_discount(self):
#     return self.compare_price is not None and self.compare_price > self.price


class ProductImage(models.Model):
    """
    Дополнительные изображения для товара (галерея).
    """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images", verbose_name="Товар"
    )
    image = models.ImageField(upload_to="products/gallery/", verbose_name="Изображение")
    position = models.PositiveIntegerField(default=0, verbose_name="Порядок")
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товаров"
        ordering = ("position",)

    def __str__(self):
        return f"Изображение для {self.product.name}"
