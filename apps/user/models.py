from django.db import models
from apps.common.models import BaseModel
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class User(AbstractUser, BaseModel):
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='user_images/', default='images/default-user-image.png')

    def __str__(self):
        if self.get_full_name():
            return f"{self.get_full_name()}"
        if self.email:
            return f"{self.email}"
        return f"{self.username}"
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'