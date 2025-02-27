from django.db import models
from django.conf import settings

# class Portfolio(models.Model):
#     student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     image = models.ImageField(upload_to="portfolio_images/", blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

from django.db import models
from django.contrib.auth.models import User

class PortfolioProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)  # 公開/非公開フラグ
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="portfolio_images/", blank=True, null=True)

    def __str__(self):
        return self.title
