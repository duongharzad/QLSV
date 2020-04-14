from django.db import models


# Create your models here.
class SubjectModel(models.Model):
    credit = models.IntegerField(null=True, blank=True)
    subject_name = models.CharField(max_length=255, null=True, blank=True, unique=True)

    class Meta:
        db_table = 'subject'
        verbose_name = 'Subject'
