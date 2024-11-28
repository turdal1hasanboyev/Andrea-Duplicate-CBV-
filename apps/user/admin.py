from django.contrib import admin
from .models import User


admin.site.site_header = "Andrea Admin Panel"
admin.site.site_title = "Andrea Admin Panel"
admin.site.index_title = "Welcome to the Andrea Administration Panel!"


admin.site.register(User)