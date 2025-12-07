from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom User model.
    We extend AbstractUser so we can add fields later (like 'is_creator')
    without breaking the database schema.
    """
    email = models.EmailField(unique=True) # make email unique/required

    # can add a flag here later for specific roles
    # is_creator = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Profile(models.Model):
    """
    Profile model for additional user information.
    Linked One-to-One with the User.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    # using a URL field for now to avoid setting up media servers immediately,
    # but normally this would be models.ImageField()
    avatar_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
