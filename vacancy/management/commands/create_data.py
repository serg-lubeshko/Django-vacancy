from django.core.management.base import BaseCommand
import importlib
from data import data
from vacancy.models import Company, Specialty, Vacancy


class Command(BaseCommand):
    # def add_arguments(self, parser):
    #     parser.add_argument('source', nargs='+', type=str)
    #https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/
    def handle(self, *args, **options):
        # module = importlib.import_module(source[0])
        for com in data.companies:
            Company.objects.create(
                name=com['title'],
                location=com['location'],
                logo=com['logo'],
                description=com['description'],
                employee_count=com['employee_count']
            )
        for spec in data.specialties:
            Specialty.objects.create(
                
            )
        # for vac in data.jobs:
        #     Vacancy.objects.create(*vac)
