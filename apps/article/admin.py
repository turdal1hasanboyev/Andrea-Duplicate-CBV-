from django.contrib import admin
from .models import Tag, Category, Article, Comment


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Comment)