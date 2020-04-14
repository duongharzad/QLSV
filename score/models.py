from django.db import models


# Create your models here.
from student.models import StudentModel
from subject.models import SubjectModel


class ScoreModel(models.Model):
    score_first = models.IntegerField(default=0)
    score_second = models.IntegerField(default=0)
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Score'
        verbose_name = 'Score'

