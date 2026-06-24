from rest_framework import serializers

from .models import MeasurementRequest


class MeasurementRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementRequest
        fields = (
            'id',
            'full_name',
            'phone',
            'email',
            'preferred_time',
            'wishes',
            'status',
            'created_at',
        )
        read_only_fields = ('status', 'created_at')

