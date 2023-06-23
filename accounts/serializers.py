from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('last_name', 'first_name', 'email', 'phone', 'date_joined', 'last_login', 'is_active', 'is_admin')


class AccountDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'phone')
        read_only_fields = ('email',)
