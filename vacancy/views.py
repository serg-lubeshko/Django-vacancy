from django.shortcuts import render


# Главная
def main_view(request):
    context = {'chapter': 'Здесь будет главная страница'}
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
