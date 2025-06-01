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

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'amount', 'transaction_type', 'category', 'wallet', 'created_at')
    search_fields = ('title', 'user__email')
    list_filter = ('transaction_type', 'created_at', 'category')
    date_hierarchy = 'created_at'
    
@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'category', 'amount', 'start_date', 'end_date')
    search_fields = ('user__email',)
    list_filter = ('category', 'start_date')
    
@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'target_amount', 'due_date', 'status')
    search_fields = ('name', 'user__email')
    list_filter = ('due_date', 'status')