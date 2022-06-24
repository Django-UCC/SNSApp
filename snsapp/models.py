from django.db import models

class PostModel(models.Model):
    author = models.CharField(max_length=50)
    content = models.TextField()
