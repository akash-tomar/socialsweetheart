from django.db import models
from social_django.models import UserSocialAuth

# Create your models here.

class AccessToken(models.Model):
    access_token = models.CharField(max_length=1000)
    social_auth = models.OneToOneField(UserSocialAuth, on_delete=models.CASCADE, related_name = 'access_token')

    class Meta:
        verbose_name_plural = "Access Tokens"

    def __str__(self):
        return str(self.id)