# home/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='home_profile')
    surname = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True, blank=True)
    location = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    employment = models.CharField(max_length=100)
    show_profile = models.BooleanField(default=True)
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', default='default.jpg')

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    class Like(models.Model):
        sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes_sent")
        receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes_received")
        created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} likes {self.receiver}"
    
    class Message(models.Model):
        sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages_sent")
        receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages_received")
        message = models.TextField()
        timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver}"