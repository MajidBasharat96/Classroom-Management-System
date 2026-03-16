
from djongo import models
from students.models import Student

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    total_marks = models.IntegerField()
    obtained_marks = models.IntegerField()
