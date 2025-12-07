from rest_framework import viewsets, permissions
from .models import AudioBook, Category, Creator
from .serializers import AudioBookSerializer, CategorySerializer, CreatorSerializer


class AudioBookViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows AudioBooks to be viewed.
    ReadOnlyModelViewSet automatically provides:
    - GET /api/audiobooks/ (List all)
    - GET /api/audiobooks/{id}/ (Get one)
    """
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer
    permission_classes = [permissions.AllowAny] # Public access for now


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class CreatorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer
    permission_classes = [permissions.AllowAny]
