from django.db import models


class Specialty(models.Model):
    code = models.IntegerField(unique=True)
    title = models.CharField(max_length=124)
    picture = models.URLField(default='https://place-hold.it/100x60')


class Company(models.Model):
    name = models.CharField(max_length=124)
    location = models.CharField(max_length=124)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.PositiveSmallIntegerField()


class Vacancy(models.Model):
    title = models.CharField(max_length=124)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=124)
    description = models.TextField()
    salary_min = models.PositiveSmallIntegerField()
    salary_max = models.PositiveSmallIntegerField()
    published_at = models.DateField(auto_now=True)
