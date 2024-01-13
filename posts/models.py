from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    media = models.FileField()
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), null=False, on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=255)
    posts = models.ManyToManyField(Post)


class Comment(models.Model):
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), null=False, on_delete=models.CASCADE)