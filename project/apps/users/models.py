from django.db import models
from django.contrib.auth.models import User
from .utils import user_directory_path

    
class Avatar(models.Model):
    user = models.OneToOneField(User, blank=False, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path) 

    def __str__(self):
        return self.user.username