from django.contrib import admin
from my_app.models import User, Tarif


class UserAdmin(admin.ModelAdmin):
    list_display = ['telegram_id', 'username', 'first_name', 'language', 'user_tarif', 'is_active', 'created_at']
    list_filter = ['language', 'user_tarif', 'is_active']
    search_fields = ['telegram_id', 'username', 'first_name', 'is_active']


admin.site.register(User, UserAdmin)


class TarifAdmin(admin.ModelAdmin):
    list_display = ['tarif_name', 'tarif_price', 'tarif_active_date', 'references']
    list_filter = ['tarif_name']
    search_fields = ['tarif_name']


admin.site.register(Tarif, TarifAdmin)
