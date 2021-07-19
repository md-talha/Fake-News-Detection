from django.db import models

# Create your models here.

class AddNews(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()