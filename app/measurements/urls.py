from django.urls import path

from .views import MeasurementRequestListCreateView


urlpatterns = [
    path('requests/', MeasurementRequestListCreateView.as_view(), name='measurement-request-list-create'),
]

