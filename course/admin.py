from django.contrib import admin


# Register your models here.
from course.models import ClassModel, TrainingSystemModel, CourseModel, FacultyModel, SubjectModel, StudentModel, \
    ScoreModel


class CourseAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'training_system', 'course', 'faculty']


class ScoreAdmin(admin.ModelAdmin):
    list_display = ['score_first', 'score_second', 'student', 'subject']


admin.site.register(ClassModel, CourseAdmin)
admin.site.register(TrainingSystemModel)
admin.site.register(CourseModel)
admin.site.register(FacultyModel)
admin.site.register(SubjectModel)
admin.site.register(StudentModel)
admin.site.register(ScoreModel, ScoreAdmin)
