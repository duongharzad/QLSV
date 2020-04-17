from random import randrange

from django.core.management import BaseCommand
from faker import Faker
from faker.generator import random

from course.models import StudentModel, CourseModel, FacultyModel, ClassModel, ScoreModel, SubjectModel

fake = Faker(['en_US'])


class Command(BaseCommand):
    help = 'Fake data'

    def add_arguments(self, parser):
        parser.add_argument('record', type=int, help='ABC')

    def handle(self, *args, **options):
        records = options['record']

        # list = ['Male', 'Female']
        #
        # list_class_model = ClassModel.objects.all()
        #
        # for _ in range(0, records):
        #     StudentModel.objects.create(
        #         student_name=fake.name(),
        #         gender=random.choice(list),
        #         address=fake.address(),
        #         student_class=random.choice(list_class_model)
        #     )

        list_subject = SubjectModel.objects.all()

        list_student = StudentModel.objects.all()

        for _ in range(0, records):
            ScoreModel.objects.create(
                score_first=randrange(5, 10),
                score_second=randrange(5, 10),
                student=random.choice(list_student),
                subject=random.choice(list_subject)
            )

