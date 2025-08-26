# home/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='home_profile')
    surname = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    employment = models.CharField(max_length=100)
    show_profile = models.BooleanField(default=True)  # To hide/unhide profiles later

    def _str_(self):
        return f"{self.user.username}'s Profile"