from django.db import models
from apps.users.models import User


class Category(models.Model):
    """Genres (Sci-Fi, Business, Romance, etc.)"""

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Creator(models.Model):
    """Authors and Narrators"""

    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class AudioBook(models.Model):
    """Main Product"""

    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    # Relationships
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="books")
    authors = models.ManyToManyField(Creator, related_name="authored_books")
    narrators = models.ManyToManyField(Creator, related_name="narrated_books", blank=True)

    # Media
    cover_image = models.ImageField(upload_to="covers/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    """Individual audio files belonging to a book."""

    book = models.ForeignKey(AudioBook, on_delete=models.CASCADE, related_name="chapters")
    title = models.CharField(max_length=255)
    sequence_order = models.PositiveIntegerField(default=1)

    # Will swap this for S3 later, but this works for local dev
    audio_file = models.FileField(upload_to="audio_files/")

    # auto-calculated later (in seconds)
    duration = models.PositiveIntegerField(default=0, help_text="Duration in seconds")

    class Meta:
        ordering = ["sequence_order"]  # default sort by chapter number

    def __str__(self):
        return f"{self.book.title} - {self.title}"
