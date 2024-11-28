from django.db import models
from apps.common.models import BaseModel
from ckeditor.fields import RichTextField


class Contact(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField(max_length=100, db_index=True, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True, unique=True)
    message = RichTextField(null=True, blank=True)

    def __str__(self):
        if self.name:
            return f"{self.name}"
        return None
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"