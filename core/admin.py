from django.contrib import admin
from .models import SiteSettings

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fields = ('primary_color',)
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()