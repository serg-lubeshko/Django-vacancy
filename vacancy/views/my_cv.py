from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from vacancy.forms import ResumeForm
from vacancy.models import Resume


class ResumeEdit(LoginRequiredMixin, View):
    def get_object(self):
        try:
            return Resume.objects.get(user_id=self.request.user.pk)
        except Resume.DoesNotExist:
            return None

    def get(self, request):
        objects = self.get_object()
        if objects is None:
            return redirect('resume_letsstart')
        form = ResumeForm(instance=objects)
        return render(request, "vacancy/resume/resume-edit.html", {"form": form})

    def post(self, request):
        objects = self.get_object()
        form = ResumeForm(request.POST, instance=objects)
        if form.is_valid():
            form.save()
            messages.success(request, 'Резюме обновлено')
            return redirect('resume_edit')
        else:
            messages.error(request, "Ошибка в обновлении данных")
            return redirect('resume_edit')


class ResumeLetsStart(TemplateView):
    template_name = "vacancy/resume/resume-create.html"


class ResumeCreate(View):
    def get(self, request):
        form = ResumeForm()
        return render(request, "vacancy/resume/resume-edit.html", {"form": form})

    def post(self, request):
        form = ResumeForm(request.POST)
        if form.is_valid():
            form_add = form.save(commit=False)
            form_add.user_id = request.user.pk
            form_add.save()
            messages.success(request, 'Резюме создано')
            return redirect('resume_edit')
        else:
            messages.error(request, "Ошибка в создании данных")
            return redirect('resume_create')
