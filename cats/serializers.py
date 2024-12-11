# Обновлённый kittygram/cats/serializers.py
from .models import Cat
from rest_framework import serializers


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ('id', 'name', 'color', 'birth_year')