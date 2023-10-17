from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
import re

User = get_user_model()

class CustomUserCreateSerializer(UserCreateSerializer):
    documento = serializers.CharField(max_length=20, required=True)
    letra_diferenciadora = serializers.CharField(max_length=1, required=False)

    class Meta(UserCreateSerializer.Meta):
        fields = ('id', 'email', 'first_name', 'last_name', 'documento', 'letra_diferenciadora', 'password', 're_password')

    def validate_documento(self, value):
        # Validar el campo "documento"
        if not value:
            raise serializers.ValidationError('El campo de documento es obligatorio.')
        if not re.match(r'^\S*[0-9]\S*$', value):
            raise serializers.ValidationError('El campo de documento debe contener al menos un número válido y no debe tener espacios en blanco.')
        return value

    def perform_create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
