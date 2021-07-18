import os

import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'conf.settings'
django.setup()

from datetime import datetime

from vacancy.models import Company, Specialty, Vacancy
from data.data import jobs, companies, specialties

if __name__ == "__main__":

    for company in companies:
        Company.objects.create(
            name=company['title'],
            location=company['location'],
            logo=company['logo'],
            description=company['description'],
            employee_count=company['employee_count']
        )
    for specialty in specialties:
        Specialty.objects.get_or_create(
            code=specialty['code'],
            title=specialty['title'],
        )
    for vacancy in jobs:
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
