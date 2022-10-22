
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, ImagesViewSet
router = DefaultRouter()

router.register('blogapi', BlogViewSet, basename="blogs")
router.register('images', ImagesViewSet, basename="image")

urlpatterns = [
    path('', include(router.urls))
]
