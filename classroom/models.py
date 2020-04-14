from django.db import models


# Create your models here.
from course.models import CourseModel
from faculty.models import FacultyModel


class TrainingSystemModel(models.Model):
    training_name = models.CharField(max_length=255, null=True, blank=True, unique=True)

    class Meta:
        db_table = 'trainingsystem'
        verbose_name = 'Training system'


class ClassModel(models.Model):
    class_name = models.CharField(max_length=255, null=True, blank=True, unique=False)
    training_system = models.ForeignKey(TrainingSystemModel, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    faculty = models.ForeignKey(FacultyModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Class'
        verbose_name = 'Class'

