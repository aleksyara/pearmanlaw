from django.db import models
from django.urls import reverse
# from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

# A User has many Posts; and a Post belongs to a User
# Import the User
from django.contrib.auth.models import User

# Create your models here.

# if we update Model (rows) -> run: 1) python3 manage.py makemigrations; 2) python3 manage.py migrate
class Post(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(max_length = 2000)
    body = RichTextField(blank=True, null=True)
    # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# It's a best practice to override the __str__ method in Models. We can return Title for now
    def __str__(self):
        return self.title

  # Add this method to display a new cat
    def get_absolute_url(self):
        return reverse('blog') #'blog' -> name attribute in urls.