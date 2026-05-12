from django.db import models
from  django.contrib.auth.models import User  
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=600)
    photo = models.ImageField(upload_to='tweet_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "{self.user.username}: {self.text[:50]}"