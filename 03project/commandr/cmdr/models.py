from django.db import models



class Employee (models.Model):
    name=models.CharField(max_length=255)
    age=models.PositiveIntegerField()
    Remarks=models.TextField()
    about=models.TextField()
    def __str__ (self):
        return self.name
