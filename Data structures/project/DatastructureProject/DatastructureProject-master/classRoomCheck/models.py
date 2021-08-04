from django.db import models

# Create your models here.

class AllClassRooM(models.Model):
    name = models.CharField(max_length=200)
    student = models.TextField()
