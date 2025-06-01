from rest_framework import serializers
from .models import Transaction, Category, Wallet, Goal, Budget

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    wallet = WalletSerializer(read_only=True)
    wallet_id = serializers.PrimaryKeyRelatedField(
        queryset=Wallet.objects.all(), source='wallet', write_only=True, required=False
    )

    class Meta:
        model = Transaction
        fields = [
            'id', 'user', 'title', 'amount', 'transaction_type',
            'category', 'category_id', 'wallet', 'wallet_id',
            'note', 'created_at', 'updated_at'
        ]
        read_only_fields = ['user', 'created_at', 'updated_at']

class BudgetSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Budget
        fields = [
            'id', 'user', 'category', 'category_id',
            'amount', 'start_date', 'end_date'
        ]
        read_only_fields = ['user']
