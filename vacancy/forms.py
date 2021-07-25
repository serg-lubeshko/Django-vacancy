from django import forms
from django.forms import ClearableFileInput

from .models import Application, Company, Vacancy, Specialty


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["written_username", "written_phone", "written_cover_letter"]
        widgets = {
            "written_username": forms.TextInput(attrs={"class": "form-control"}),
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
        fields = ["name", "location", "logo", "description", "employee_count"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "employee_count": forms.TextInput(attrs={"class": "form-control"}),
            "logo": ClearableFileInput(),
        }


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        specialty = forms.ModelChoiceField(queryset=None)
        fields = ["title", "specialty", "salary_min", "salary_max", "skills", "description"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "specialty": forms.Select(attrs={"class": "form-control"}),
            "salary_min": forms.NumberInput(attrs={"class": "form-control"}),
            "salary_max": forms.NumberInput(attrs={"class": "form-control"}),
            "skills": forms.Textarea(attrs={"class": "form-control", 'rows': 4}),
            "description": forms.Textarea(attrs={"class": "form-control"}),


        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['specialty':str].queryset = Specialty.objects.all()
