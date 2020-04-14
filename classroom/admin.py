from django.contrib import admin

# Register your models here.
from classroom.models import ClassModel, TrainingSystemModel


class ClassAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'training_system', 'course', 'faculty']


admin.site.register(ClassModel, ClassAdmin)
admin.site.register(TrainingSystemModel)
