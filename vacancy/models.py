from django.contrib.auth.models import User
from django.db import models


# Для заполнения БД можно использовать script.py либо
# python manage.py create_data - заполняем данными из data.py
class Specialty(models.Model):
    code = models.CharField(max_length=124, primary_key=True)
    title = models.CharField(max_length=124)
    # picture = models.URLField(default='https://place-hold.it/100x60')
    picture = models.ImageField(upload_to="picture")

    def __str__(self):
        return self.title


# Для заполнения БД можно использовать script.py либо
# python manage.py create_data - заполняем данными из data.py

class Company(models.Model):
    name = models.CharField(max_length=124)
    location = models.CharField(max_length=124)
    logo = models.ImageField(upload_to="logo")
    description = models.TextField()
    employee_count = models.PositiveSmallIntegerField()
    owner = models.OneToOneField(User, on_delete=models.SET_NULL, related_name="applications", null=True)

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
    published_at = models.DateField(auto_now=True)

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


# модель «Resume – резюме» с полями:
class Resume(models.Model):
    """

– Пользователь (user, связь с User, тип поля: OneToOneField)
– Имя (name)
– Фамилия (surname)
– Готовность к работе (status) – Не ищу работу – Рассматриваю предложения – Ищу работу
– Вознаграждение (salary)
– Специализация (specialty)
– Квалификация (grade)  – Стажер – Джуниор – Миддл – Синьор — Лид
– Образование (education)
– Опыт работы (experience)
– Портфолио (portfolio)                            +
    """
    RESTING = 'RG'
    CONSIDER = 'CR'
    SEEK = 'SK'
    STATUS_IN_RESUME = [
        (RESTING, 'Не ищу работу'),
        (CONSIDER, 'Рассматриваю предложения'),
        (SEEK, 'Ищу работу'),
        
    ]

    TRAINEE = 'TE'
    JUNIOR = 'JR'
    MIDL = 'ML'
    SENIOR = 'SR'
    LEAD = 'LD'
    GRADE_IN_RESUME = [
        (TRAINEE, 'Стажер'),
        (JUNIOR, 'Джуниор'),
        (MIDL, 'Миддл'),
        (SENIOR, 'Синьор'),
        (LEAD, 'Лид'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="resume_user")
    name = models.CharField(max_length=124, verbose_name="Имя")
    surname = models.CharField(max_length=124, verbose_name="Фамилия")
    status = models.CharField(max_length=2, choices=STATUS_IN_RESUME, default=SEEK, verbose_name="Готовность к работ")
    salary = models.PositiveSmallIntegerField(verbose_name="Вознаграждение")
    specialty = models.ForeignKey(Specialty,
                                  on_delete=models.CASCADE,
                                  related_name="resume",
                                  verbose_name="Специализация")
    grade = models.CharField(max_length=2, choices=GRADE_IN_RESUME, default=TRAINEE, verbose_name="Квалификация")
    education = models.TextField(verbose_name="Образование")
    experience = models.TextField(verbose_name="Опыт работы")
    portfolio = models.URLField(blank=True, verbose_name="Портфолио")

    def __str__(self):
        return f"{self.name} {self.surname}"
