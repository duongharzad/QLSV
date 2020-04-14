from django.db import models


# Create your models here.
class FacultyModel(models.Model):
    faculty_name = models.CharField(max_length=255, null=True, blank=True, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True, unique=False)

    class Meta:
        db_table = 'Faculty'
        verbose_name = 'Faculty'
