from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime

class Progress(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    # def get_iso_format(self):
    #     if isinstance(self.created_at, datetime):
    #         return self.created_at.isoformat()
    #     if isinstance(self.updated_at, datetime):
    #         return self.updated_at.isoformat()

    def __str__(self):
        return self.title
