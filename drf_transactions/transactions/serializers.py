from rest_framework import serializers
from transactions.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['created', 'price', 'quantity', 'order_price', 'symbol']
