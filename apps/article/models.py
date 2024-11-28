from django.db import models
from apps.common.models import BaseModel
from django.utils.text import slugify
import uuid
from ckeditor.fields import RichTextField
from django.urls import reverse
from apps.user.models import User


class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, db_index=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = f"{slugify(self.name)}-{uuid.uuid4()}"
        super().save(*args, **kwargs)


class Tag(BaseModel):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, db_index=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
    
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Article(BaseModel):
    name = models.CharField(max_length=250, db_index=True, unique=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True, db_index=True)
    image = models.ImageField(upload_to="articles_images", default='images/default-image.png')
    description = RichTextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="articles_category")
    author = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name="articles_author")
    tags = models.ManyToManyField(to=Tag, blank=True, related_name="articles_tags")
    views = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = f"{slugify(self.name)}-{uuid.uuid4()}"
        super().save(*args, **kwargs)
    
    def get_absolute_url(self, *args, **kwargs):
        return reverse('single', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"


class Comment(BaseModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments_article")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments_user")
    name = models.CharField(max_length=225, db_index=True)
    email = models.EmailField(max_length=125, db_index=True, null=True, blank=True)
    web_site = models.URLField(max_length=200, unique=True, null=True, blank=True, db_index=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"