from rest_framework import generics, permissions

from .models import MeasurementRequest
from .serializers import MeasurementRequestSerializer


class MeasurementRequestListCreateView(generics.ListCreateAPIView):
    serializer_class = MeasurementRequestSerializer

    def get_queryset(self):
        return MeasurementRequest.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

