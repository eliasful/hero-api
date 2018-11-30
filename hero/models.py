from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    photo = models.TextField(blank=True, null=True)
    favorite = models.BooleanField(default=False)


    def __str__(self):
        return self.name
