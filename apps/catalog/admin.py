from django.contrib import admin
from .models import Category, Creator, AudioBook, Chapter


class ChapterInline(admin.TabularInline):
    """allows to add chapters directly inside the audiobook page"""

    model = Chapter
    extra = 1


@admin.register(AudioBook)
class AudioBookAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "price"]
    list_filter = ["category"]
    search_fields = ["title"]
    inlines = [ChapterInline]


admin.site.register(Category)
admin.site.register(Creator)
