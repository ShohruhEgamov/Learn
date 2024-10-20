from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Blog(models.Model):
    titles = models.CharField(max_length=100)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.titles