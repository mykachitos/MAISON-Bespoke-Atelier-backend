from rest_framework import serializers
from .models import EditorDesign


class DesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = EditorDesign
        fields = '__all__'
        read_only_fields = ('user',)