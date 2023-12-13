from django.db import models

# Create your models here.
class Court(models.Model):
  name = models.CharField(max_length=255)
  surface = models.CharField(max_length=255)
  location = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.name} {self.location}"