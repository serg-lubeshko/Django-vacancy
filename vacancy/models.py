from django.contrib.auth.models import User
from django.db import models


# Для заполнения БД можно использовать script.py либо
# python manage.py create_data - заполняем данными из data.py
class Specialty(models.Model):
    code = models.CharField(max_length=124, primary_key=True)
    title = models.CharField(max_length=124)
    # picture = models.URLField(default='https://place-hold.it/100x60')
    picture = models.ImageField(upload_to="media")

    def __str__(self):
        return self.title


# Для заполнения БД можно использовать script.py либо
# python manage.py create_data - заполняем данными из data.py
class Company(models.Model):
    name = models.CharField(max_length=124)
    location = models.CharField(max_length=124)
    logo = models.ImageField(upload_to="media")
    description = models.TextField()
    employee_count = models.PositiveSmallIntegerField()
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="applications", null=True)

    def __str__(self):
        return self.name.title()

# Для заполнения БД можно использовать script.py либо
# python manage.py create_data - заполняем данными из data.py
class Vacancy(models.Model):
    title = models.CharField(max_length=124)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=124)
    description = models.TextField()
    salary_min = models.PositiveSmallIntegerField()
    salary_max = models.PositiveSmallIntegerField()
    published_at = models.DateField()

    def __str__(self):
        return self.title


class Application(models.Model):
    written_username = models.CharField(max_length=100, verbose_name="Имя")
    written_phone = models.CharField(max_length=20, verbose_name="Телефон")
    written_cover_letter = models.TextField(verbose_name="Сопроводительное письмо")
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, verbose_name="Вакансия", related_name="applications")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь",
                             related_name="applications_user")


    def __str__(self):
        return f'Отклик {self.pk}: {self.written_username}'
