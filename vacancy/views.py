from django.db.models import Count
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from django.views.generic import UpdateView

from vacancy.forms import ApplicationForm, CompanyForms
from vacancy.models import Specialty, Company, Vacancy, Application


# Главная
def main_view(request):
    specializations = Specialty.objects.annotate(count_vacancies_specialty=Count('vacancies'))
    companies = Company.objects.annotate(count_vacancies_company=Count('vacancies')).order_by(
        '-count_vacancies_company')
    context = {
        'specializations': specializations,
        'companies': companies,

    }
    return render(request, template_name='vacancy/index.html', context=context)


# Все вакансии списком
def show_list_all_vacancies(request):
    vacancies = Vacancy.objects.order_by('-published_at')
    context = {
        'vacancies': vacancies,
        'count_vacansies': vacancies.count(),
        'chapter': 'Все вакансии',
    }
    return render(request, template_name='vacancy/vacancies.html', context=context)


# Вакансии по специализации
def show_list_specialty_vacancies(request, specialty):
    get_object_or_404(Specialty, code=specialty)
    vacancies = Vacancy.objects.filter(specialty=specialty).order_by('-published_at')
    context = {
        'vacancies': vacancies,
        'count_vacansies': vacancies.count(),
        'chapter': specialty,
    }
    return render(request, template_name='vacancy/vacancies.html', context=context)


# Карточка компании
def card_company_view(request, pk):
    try:
        company = Company.objects.get(pk=pk)
        company_vacancies = company.vacancies.select_related('specialty').all()
    except Company.DoesNotExist:
        raise Http404
    context = {
        "company_vacancies": company_vacancies,
        'company': company,
        'count_vacansies': company_vacancies.count()
    }
    return render(request, template_name='vacancy/company.html', context=context)


# Одна вакансия
def vacancy_view(request, pk):
    form = ApplicationForm()
    try:
        vacancy = Vacancy.objects.select_related('company').get(pk=pk)
        vacancy_id = pk
    except Vacancy.DoesNotExist:
        raise Http404
    context = {
        'vacancy': vacancy,
        'form': form
    }

    if request.method == "POST":
        if request.user.is_authenticated:
            form = ApplicationForm(request.POST)
            if form.is_valid():
                user_id = request.user.pk
                user_vacancy_add = {"user_id": user_id, "vacancy_id": vacancy_id}
                Application.objects.filter(user_id=user_id, vacancy_id=vacancy_id).delete()
                Application.objects.create(**form.cleaned_data, **user_vacancy_add)
                return redirect('sent')
        else:
            print("НАПРАВИТЬ НА РЕГИСТРАЦИЮ")
    return render(request, template_name='vacancy/vacancy.html', context=context)


# перенаправления на sent.html. "Отклик отправлен"
def sent(request):
    get_url = request.META.get('HTTP_REFERER')
    return render(request, template_name="vacancy/sent.html", context={"get_url": get_url})


# Заполненная форма компании
def mycompany(request):
    form = CompanyForms()
    try:
        a = Company.objects.get(owner_id=request.user.pk)
    except:
        print('NO')
        form = CompanyForms(instance=a)
        img =a.logo
        print(form)
        # if request.method == "GET":
        #     company_user = Company.objects.get(owner_id=request.user.pk)
        #     print(company_user.name)
    return render(request, template_name="vacancy/company-edit.html", context={'form': form, 'img':img})

# class CompanyUpdate(View):
#     template_name = "vacancy/company-edit.html"
#     def get_object(self):
#         print('hello')


#
# class AuthorUpdateView(UpdateView):
#     model = Company
#     fields = ['name']
#     template_name_suffix = '_update_form'
