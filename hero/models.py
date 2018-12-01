from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    favorite = models.BooleanField(default=False)
    photo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
