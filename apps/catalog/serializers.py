from rest_framework import serializers
from .models import Category, Creator, AudioBook, Chapter


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]


class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = ["id", "name"]


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ["id", "title", "sequence_order", "duration", "audio_file"]


class AudioBookSerializer(serializers.ModelSerializer):

    # run these fields through their own serializers
    category = CategorySerializer(read_only=True)
    authors = CreatorSerializer(many=True, read_only=True)
    narrators = CreatorSerializer(many=True, read_only=True)
    chapters = ChapterSerializer(many=True, read_only=True)

    class Meta:
        model = AudioBook
        fields = [
            "id", "title", "description", "price",
            "category", "authors", "narrators",
            "cover_image", "chapters"
        ]
