from django import forms
from .models import Application, Company


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["written_username", "written_phone", "written_cover_letter"]
        widgets = {
            "written_username": forms.TextInput(attrs= {"class":"form-control"}),
            "written_phone": forms.TextInput(attrs={"class": "form-control"}),
            "written_cover_letter": forms.Textarea(attrs={"class": "form-control"}),
        }
        labels = {
            "written_username": "Вас зовут",
            "written_phone": "Ваш телефон",
            "written_cover_letter": "Сопроводительное письмо"
        }


class CompanyForms(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["name", "location", "logo", "description", "employee_count", "owner"]
        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "employee_count": forms.TextInput(attrs={"class": "form-control"}),
            # "logo": forms.ImageField(),
        }