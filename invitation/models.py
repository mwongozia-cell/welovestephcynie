from django.contrib.auth.models import User
from django.db import models

class RSVP(models.Model):
    name = models.CharField(max_length=100)
    rsvp_type = models.CharField(max_length=20)
    count = models.PositiveIntegerField(default=1)
    attendees = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.rsvp_type})"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    instagram = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
