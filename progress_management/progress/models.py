# from django.db import models
# from django.contrib.auth.models import User
# from django.conf import settings
# from datetime import datetime

# class Progress(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
        
#     def __str__(self):
#         return self.title

from django.db import models
from django.conf import settings

class Game(models.Model):
    name = models.CharField(max_length=200)
    plan_image = models.ImageField(upload_to='plans/', blank=True, null=True)
    plan_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Progress(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='progresses', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    question1 = models.CharField(max_length=255, blank=True, null=True)
    question2 = models.CharField(max_length=255, blank=True, null=True)
    question3 = models.CharField(max_length=255, blank=True, null=True)
    question4 = models.CharField(max_length=255, blank=True, null=True)
    question5 = models.CharField(max_length=255, blank=True, null=True)
    question6 = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.title
