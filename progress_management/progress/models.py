from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime

class Progress(models.Model):
    title = models.CharField(max_length=200)
    description1 = models.TextField()
    description2 = models.TextField(default="")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.title
    
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    test = models.TextField(default="test", verbose_name="test", blank=False, null=False, editable=True, max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class SubPage(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    progress_title = models.CharField(max_length=200)
    progress_detail = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.game.title} - {self.progress_title}"
    
    
# from django.db import models

# class Plan(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

# class GamePlan(models.Model):
#     game = models.OneToOneField(Plan, on_delete=models.CASCADE, related_name='plan')
#     concept = models.TextField()
#     mechanics = models.TextField()
#     art_style = models.TextField()
#     development_schedule = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
