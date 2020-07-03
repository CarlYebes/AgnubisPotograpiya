from django.db import models

# Deletes the image when data in database is deleted
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.

class picture(models.Model):
    title = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=200, blank=True)
    image = models.ImageField()
    id = models.PositiveIntegerField(primary_key=True)

    def __str__(self):
        return f"{self.id} - {self.title}"


# Deletes the image when data in database is deleted
@receiver(post_delete, sender=picture)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)
