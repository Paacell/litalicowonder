from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

class GamePlan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)  # ユーザー情報を追加
    title = models.CharField(max_length=255)
    description1 = models.TextField(default="", null=False, blank=False)
    description2 = models.TextField(default="", null=False, blank=False)
    description3 = models.TextField(default="", null=False, blank=False)
    description4 = models.TextField(default="", null=False, blank=False)
    description5 = models.TextField(default="", null=False, blank=False)
    image = models.ImageField(upload_to='game_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    game_plan = models.ForeignKey(GamePlan, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20,
        choices=[
            ('not_started', '未着手'),
            ('in_progress', '実行中'),
            ('completed', '完了'),
        ],
        default='not_started'
    )

class Feedback(models.Model):
    game_plan = models.ForeignKey('GamePlan', on_delete=models.CASCADE, related_name='feedbacks', default=None, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=False, null=False)  # ユーザー情報を追加    game_plan = models.ForeignKey('GamePlan', on_delete=models.CASCADE, related_name='feedbacks')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.game_plan.title} on {self.created_at.strftime('%Y-%m-%d')}"