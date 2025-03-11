from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime

class Progress(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.title
    
class SubPage(models.Model):
    print("test")
    game = models.ForeignKey(Progress, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    design_document = models.ImageField(upload_to='design_documents/')
    progress_note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.game.title} - {self.title}"
