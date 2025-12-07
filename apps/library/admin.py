from django.contrib import admin
from .models import LibraryItem, ListeningProgress


@admin.register(LibraryItem)
class LibraryItemAdmin(admin.ModelAdmin):
    list_display = ["user", "audiobook", "purchase_date"]
    list_filter = ["purchase_date"]
    search_fields = ["user__username", "audiobook__title"]


@admin.register(ListeningProgress)
class ListeningProgressAdmin(admin.ModelAdmin):
    list_display = ["user", "chapter", "current_timestamp", "is_finished", "last_updated"]
    list_filter = ["is_finished"]
