from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=191)
    student_id = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.name} ({self.student_id}) <{self.email}>"