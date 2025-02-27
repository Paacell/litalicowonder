from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=True)  # 生徒フラグ
    is_admin = models.BooleanField(default=False)  # 管理者フラグ


# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#     USER_TYPE_CHOICES = (
#         ('student', 'Student'),
#         ('admin', 'Admin'),
#     )
#     user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='student')


