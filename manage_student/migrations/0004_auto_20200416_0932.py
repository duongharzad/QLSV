# Generated by Django 3.0.5 on 2020-04-16 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_student', '0003_auto_20200416_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coursemodel',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
