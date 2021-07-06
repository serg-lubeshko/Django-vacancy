from django.shortcuts import render


def main_view(request):
    return render(request, template_name='vacancy/index.html')


def show_list_all_vacancies(request):
    return render(request, template_name='vacancy/vacancy-list.html')


def show_list_specialty_vacancies(request, vacancy):
    return render(request, template_name='vacancy/vacancy.html')
