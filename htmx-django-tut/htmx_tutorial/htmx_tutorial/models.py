from django.db import models

# Create your models here.

class SampleModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    favourite_color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
