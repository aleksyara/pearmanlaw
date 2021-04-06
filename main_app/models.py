from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# if we add or change Model (rows) we need to update -> run 1) python3 manage.py makemigrations; 2) python3 manage.py migrate
# class Post(models.Model):
#     title = models.CharField(max_length = 100)
#     description = models.TextField(max_length = 250)
#     # Add the foreign key linking to a user instance
#     # user = models.ForeignKey(User, on_delete=models.CASCADE)

# posts = [
#   Post('About COVID-19', 'We have already written the code to respond using the render method in the view.'),
#   Post('US Benefits', 'Now the fun stuff. We will type it in if there is time, otherwise we will copy/paste and review:')
# ]