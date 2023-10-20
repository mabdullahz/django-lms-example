from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=191)
    description = models.TextField()
    instructor =  models.CharField(max_length=191)
    code = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.title} ({self.instructor})"
