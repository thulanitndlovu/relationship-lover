from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='isosha_profile')
    bio = models.TextField(blank=True)
    age = models.IntegerField(null=True, blank=True)
    province = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    is_visible = models.BooleanField(default=True)  # Hide/unhide profile

    def _str_(self):
        return self.user.username

class Like(models.Model):
    from_user = models.ForeignKey(User, related_name='liker', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='liked', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.from_user} liked {self.to_user}"

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.sender} to {self.receiver}: {self.content[:30]}"