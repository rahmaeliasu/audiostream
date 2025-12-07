from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AudioBookViewSet, CategoryViewSet, CreatorViewSet

# register viewsets with router
router = DefaultRouter()
router.register(r'audiobooks', AudioBookViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'creators', CreatorViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
