from django.db import models


# Create your models here.

class TrainingSystemModel(models.Model):
    training_name = models.CharField(max_length=255, null=True, blank=True, unique=True)

    def __str__(self):
        return self.training_name

    class Meta:
        verbose_name = 'Training system'


class CourseModel(models.Model):
    course_name = models.CharField(max_length=255, null=True, blank=True, unique=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = 'Course'


class FacultyModel(models.Model):
    faculty_name = models.CharField(max_length=255, null=True, blank=True, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True, unique=False)

    def __str__(self):
        return self.faculty_name

    class Meta:
        db_table = 'Faculty'
        verbose_name = 'Faculty'


class ClassModel(models.Model):
    class_name = models.CharField(max_length=255, null=True, blank=True, unique=False)
    training_system = models.ForeignKey(TrainingSystemModel, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    faculty = models.ForeignKey(FacultyModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.class_name

    class Meta:
        db_table = 'Class'
        verbose_name = 'Class'


class SubjectModel(models.Model):
    credit = models.IntegerField(null=True, blank=True)
    subject_name = models.CharField(max_length=255, null=True, blank=True, unique=True)

    def __str__(self):
        return self.subject_name

    class Meta:
        db_table = 'subject'
        verbose_name = 'Subject'


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

    def __str__(self):
        return self.student_name

    class Meta:
        db_table = 'student'
        verbose_name = 'Student'


class ScoreModel(models.Model):
    score_first = models.IntegerField(default=0)
    score_second = models.IntegerField(default=0)
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Score'
        verbose_name = 'Score'
