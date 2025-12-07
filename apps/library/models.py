from django.db import models
from django.conf import settings
from apps.catalog.models import AudioBook, Chapter


class LibraryItem(models.Model):
    """
    Represents a book owned by a user.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="library")
    audiobook = models.ForeignKey(AudioBook, on_delete=models.CASCADE, related_name="library_items")
    purchase_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["user", "audiobook"] # A user can't buy the same book twice
        ordering = ["-purchase_date"]

    def __str__(self):
        return f"{self.user.username} - {self.audiobook.title}"


class ListeningProgress(models.Model):
    """
    Tracks exactly where a user stopped listening.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="progress")
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    # store position in seconds (e.g., 125 seconds = 2 min 5 sec)
    current_timestamp = models.PositiveIntegerField(default=False)

    is_finished = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True) # updates every time user pause

    class Meta:
        # A user only has one progress record per chapter
        unique_together = ["user", "chapter"]
        ordering = ["-last_updated"]

    def __str__(self):
        return f"{self.user.username} - {self.chapter.title} ({self.current_timestamp}s)"
