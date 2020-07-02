from django.db import models

# Create your models here.

class picture(models.Model):
    title = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=200, blank=True)
    image = models.ImageField()