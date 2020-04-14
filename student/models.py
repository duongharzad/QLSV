from django.db import models

# Create your models here.
from classroom.models import ClassModel

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)


class StudentModel(models.Model):
    student_name = models.CharField(max_length=255, null=False, blank=True, unique=False)
    gender = models.CharField(choices=GENDER_CHOICES, default='', max_length=128)
    date = models.DateTimeField(null=True, blank=True)
    address = models.CharField(max_length=255, null=False, blank=True, unique=False)
    student_class = models.ForeignKey(ClassModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'student'
        verbose_name = 'Student'
