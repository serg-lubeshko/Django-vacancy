from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView

from vacancy.forms import ApplicationForm, VacancyForm
from vacancy.models import Company, Vacancy, Application


class VacancyResponse(View):
    def get_user(self):
        return self.request.user.pk

    def get(self, request, pk):
        vacancy = get_object_or_404(Vacancy.objects.select_related('company'), pk=pk)
        form = ApplicationForm()
        context = {'vacancy': vacancy, 'form': form}
        return render(request, template_name='vacancy/vacancies/vacancy.html', context=context)

    def post(self, request, pk):
        if request.user.is_authenticated:
            form = ApplicationForm(request.POST)
            if form.is_valid():
                user_id = self.get_user()
                user_vacancy_add = {"user_id": user_id, "vacancy_id": pk}
                Application.objects.filter(user_id=user_id, vacancy_id=pk).delete()
                Application.objects.create(**form.cleaned_data, **user_vacancy_add)
                return redirect('sent')
        else:
            return redirect('login')


# перенаправления на sent.html. "Отклик отправлен"
def sent(request):
    get_url = request.META.get('HTTP_REFERER')
    return render(request, template_name="vacancy/sent.html", context={"get_url": get_url})


class VacancyListCompany(LoginRequiredMixin, ListView):
    model = Vacancy
    template_name = "vacancy/vacancies/vacancy-list.html"
    context_object_name = "vacancies"

    def get_queryset(self, **kwargs):
        try:
            company = Company.objects.get(owner_id=self.request.user.pk).pk
            return Vacancy.objects.filter(company_id=company).annotate(summs=Count("applications"))
        except Company.DoesNotExist:
            return redirect("vacancy_create")


class VacancyEdit(LoginRequiredMixin, View):
    def get_object(self, **kwargs):
        return get_object_or_404(Vacancy, pk=self.kwargs['vacancy_id'])

    def get(self, request, vacancy_id):
        objects = self.get_object()
        form = VacancyForm(instance=objects)
        reviews = Application.objects.filter(vacancy_id=vacancy_id)
        context = {'reviews': reviews, "form": form, 'review': 'Отклики -'}
        return render(request=request, template_name="vacancy/vacancies/vacancy-edit.html", context=context)

    def post(self, request, vacancy_id):
        objects = self.get_object()
        object_pk = objects.pk
        company = objects.company_id
        form = VacancyForm(request.POST)
        if form.is_valid():
            form_add = form.save(commit=False)
            form_add.company_id = company
            form_add.id = object_pk
            form_add.save()
            messages.success(request, 'Вакансия обновлена')
            return redirect('vacancy_edit', vacancy_id)
        else:
            messages.error(request, "Ошибка в обновлении данных")
            return redirect('vacancy_edit', vacancy_id)


class VacancyCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = VacancyForm()
        context = {"form": form}
        return render(request=request, template_name="vacancy/vacancies/vacancy-edit.html", context=context)


# Поиск вакансий

class VacancySearch(ListView):
    model = Vacancy
    template_name = "vacancy/search.html"

    def get_queryset(self):
        query = self.request.GET.get('s')
        if query == "":
            object_list = Vacancy.objects.none()
        else:
            object_list = Vacancy.objects.filter(
                Q(title__icontains=query) | Q(title__icontains=query.lower()) | Q(title__icontains=query.upper()) | Q(
                    title__icontains=query.title()) |
                Q(skills__icontains=query) | Q(skills__icontains=query.lower()) | Q(
                    skills__icontains=query.upper()) | Q(
                    skills__icontains=query.title()) |
                Q(description__icontains=query) | Q(description__icontains=query.lower()) | Q(
                    description__icontains=query.upper()) | Q(description__icontains=query.title())).order_by(
                "-published_at")
        return object_list
