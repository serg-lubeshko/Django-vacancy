from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.views import View

from vacancy.forms import CompanyForms
from vacancy.models import Company


# Заполненная форма компании
class Mycompany(SuccessMessageMixin, LoginRequiredMixin, View):

    def get_object(self):
        user = self.request.user.pk
        try:
            company_user = Company.objects.get(owner_id=user)
            return company_user
        except Company.DoesNotExist:
            return None

    def get(self, request):
        objects = self.get_object()
        if objects is None:
            return redirect('letsstart')
        form = CompanyForms(instance=objects)
        img = objects.logo
        return render(request, template_name="vacancy/company/company-edit.html", context={'form': form, 'img': img})

    def post(self, request):
        objects = self.get_object()
        form = CompanyForms(request.POST, request.FILES, instance=objects)
        if form.is_valid():
            messages.success(request, 'Данные изменены успешно')
            form.save()
            return self.get(request)
        else:
            messages.error(request, 'Некорректные данные')
            form = CompanyForms(instance=objects)
            img = objects.logo
        return render(request, template_name="vacancy/company/company-edit.html", context={'form': form, 'img': img})


class CompanyLetsStart(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, template_name="vacancy/company/company-create.html")


class CompanyCreate(SuccessMessageMixin, LoginRequiredMixin, View):
    def get_object(self):
        return self.request.user.pk

    def get(self, request):
        form = CompanyForms()
        return render(request, template_name="vacancy/company/company-edit.html", context={'form': form})

    def post(self, request):
        objects = self.get_object()
        form = CompanyForms(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, 'Компания создана успешно')
            form_add = form.save(commit=False)
            form_add.owner_id = objects
            form_add.save()
            return redirect("mycompany")
        else:
            messages.error(request, 'Некорректные данные')
        return render(request, template_name="vacancy/company/company-edit.html", context={'form': form})
