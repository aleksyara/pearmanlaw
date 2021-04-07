from django.contrib import admin

# Register your models here.
# import your models here
from .models import Post

# Register your models here
admin.site.register(Post)