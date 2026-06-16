from django.db import models
from django.contrib.auth.models import User


class EditorDesign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='designs')
    name = models.CharField(max_length=200, default='Без названия')
    config = models.JSONField()
    preview = models.ImageField(upload_to='designs/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)