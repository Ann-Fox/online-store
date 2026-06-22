from django.contrib import admin
from .models import User, CustomerProfile, ManagerProfile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    pass
    # list_display = ("user", "bonus_balance", "birth_date")
    # search_fields = ("user__email", "user__username")
    # raw_id_fields = ("user",)  # удобно при большом количестве пользователей


@admin.register(ManagerProfile)
class ManagerProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "department")
    search_fields = ("user__email", "user__username")
    raw_id_fields = ("user",)
    ordering = ("-created_at",)

    @admin.display(description="ФИО")
    def user_full_name(self, obj):
        return obj.user.get_full_name()
