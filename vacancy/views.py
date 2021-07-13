from django.db.models import Count
from django.shortcuts import render

from vacancy.models import Specialty, Company, Vacancy


# Главная
def main_view(request):
    specializations = Specialty.objects.annotate(count_vacancies_specialty=Count('vacancies'))
    companies = Company.objects.annotate(count_vacancies_company=Count('vacancies')).order_by(
        '-count_vacancies_company')[:8]
    # companies_vacancies = companies.annotate(count_vacancies_company=Count('vacancies'))
    # companies_vacancies = Vacancy.objects.annotate(count_vacancies_company=Count('company_id')).order_by('-count_vacancies_company')

    print(companies.values())
    context = {
        'specializations': specializations,
        'companies': companies,
        # 'companies_vacancies': companies_vacancies,

    }
    return render(request, template_name='vacancy/index.html', context=context)


# Все вакансии списком
def show_list_all_vacancies(request):
    context = {'chapter': 'Здесь будут все вакансии списком'}
    return render(request, template_name='vacancy/vacancies.html', context=context)


# Вакансии по специализации
def show_list_specialty_vacancies(request, specialty):
    context = {'chapter': 'Здесь будут вакансии по специализации'}
    return render(request, template_name='vacancy/vacancies.html', context=context)


# Карточка компании
def card_company_view(request, pk):
    context = {'chapter': 'Здесь будет карточка компании'}
    return render(request, template_name='vacancy/company.html', context=context)


# Одна вакансия
def vacancy_view(request, pk):
    context = {'chapter': 'Здесь будет одна вакансия'}
    return render(request, template_name='vacancy/vacancy.html', context=context)
