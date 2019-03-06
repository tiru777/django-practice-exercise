from django.db import models
from django.urls import reverse
# Create your models here.

class Blog (models.Model):
    author=models.ForeignKey(
    'auth.User',
    on_delete=models.CASCADE,
    )

    title=models.CharField(max_length=250)
    text=models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
