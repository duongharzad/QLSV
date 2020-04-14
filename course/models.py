from django.db import models


# Create your models here.
class CourseModel(models.Model):
    course_name = models.CharField(max_length=255, null=True, blank=True, unique=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)



