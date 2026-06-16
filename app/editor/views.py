from rest_framework import viewsets, permissions
from .models import EditorDesign
from .serializers import DesignSerializer


class DesignViewSet(viewsets.ModelViewSet):
    serializer_class = DesignSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return EditorDesign.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)