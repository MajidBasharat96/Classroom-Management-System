
from djongo import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    roll_number = models.CharField(max_length=50)
    student_class = models.CharField(max_length=50)
    parent_contact = models.CharField(max_length=20)

    def __str__(self):
        return self.name
