from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Transaction, Category, Wallet, Goal, Budget

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'balance', 'created_at')
    search_fields = ('name', 'user__email')
    list_filter = ('created_at',)
