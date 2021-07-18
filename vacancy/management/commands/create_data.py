from datetime import datetime

from django.core.management.base import BaseCommand
from data import data
from vacancy.models import Company, Specialty, Vacancy


class Command(BaseCommand):
    def handle(self, *args, **options):
        for company in data.companies:
            Company.objects.create(
                name=company['title'],
                location=company['location'],
                logo=company['logo'],
                description=company['description'],
                employee_count=company['employee_count']
            )
        for specialty in data.specialties:
            Specialty.objects.get_or_create(
                code=specialty['code'],
                title=specialty['title'],
            )
        for vacancy in data.jobs:
            Vacancy.objects.create(
                title=vacancy['title'],
                specialty_id=vacancy['specialty'],
                company_id=vacancy['company'],
                skills=vacancy['skills'],
                description=vacancy['description'],
                salary_min=vacancy['salary_from'],
                salary_max=vacancy['salary_to'],
                published_at=datetime.strptime(vacancy['posted'], "%Y-%m-%d"),
            )
