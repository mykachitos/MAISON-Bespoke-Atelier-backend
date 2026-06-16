from rest_framework.routers import DefaultRouter
from .views import DesignViewSet

router = DefaultRouter()
router.register('designs', DesignViewSet, basename='design')
urlpatterns = router.urls