# from django.db import models

# class Goal(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title


from django.db import models
from accounts.models import CustomUser  # 生徒のアカウントを参照

class Goal(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="goals", null=True, blank=True)  # 生徒との紐付け
    title = models.CharField(max_length=255)
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.username} - {self.title}"
