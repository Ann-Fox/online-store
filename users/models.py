from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=32, blank=True, verbose_name="Телефон")
    avatar = models.ImageField(
        upload_to="users/avatars/", blank=True, verbose_name="Аватар"
    )

    class Meta(AbstractUser.Meta):
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class CustomerProfile(models.Model):
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="customer_profile",
        verbose_name="Покупатель",
    )

    birth_date = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    bonus_balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, verbose_name="Бонусный баланс"
    )
    email_verified = models.BooleanField(
        default=False, verbose_name="Email подтверждён"
    )
    phone_verified = models.BooleanField(
        default=False, verbose_name="Телефон подтверждён"
    )
    subscribe_newsletter = models.BooleanField(
        default=True, verbose_name="Подписка на новости"
    )
    subscribe_sms = models.BooleanField(default=False, verbose_name="Подписка на SMS")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Профиль создан")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Профиль обновлен"
    )

    class Meta:
        verbose_name = "Профиль покупателя"
        verbose_name_plural = "Профили покупателей"

    def __str__(self):
        return self.user.get_full_name()


class ManagerProfile(models.Model):
    class RoleChoices(models.TextChoices):
        MANAGER = "manager", "Менеджер"
        ADMIN = "admin", "Администратор"
        SUPPORT = "support", "Поддержка"
        CONTENT = "content", "Контент-менеджер"

    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="manager_profile",
        verbose_name="Менеджер",
    )

    role = models.CharField(
        max_length=20,
        choices=RoleChoices.choices,
        default=RoleChoices.MANAGER,
        verbose_name="Роль в компании",
    )
    department = models.CharField(max_length=100, blank=True, verbose_name="Отдел")
    position = models.CharField(max_length=100, blank=True, verbose_name="Должность")
    hire_date = models.DateField(
        blank=True, null=True, verbose_name="Дата приёма на работу"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Профиль создан")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Профиль обновлен"
    )
    notes = models.TextField(blank=True, verbose_name="Заметки")

    class Meta:
        verbose_name = "Профиль менеджера/администратора"
        verbose_name_plural = "Профили менеджеров/администраторов"

    def __str__(self):
        return self.user.get_full_name()
