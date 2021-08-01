from django.contrib import admin

from .models import Company, Vacancy, Application, Specialty, Resume

admin.site.register(Company)
admin.site.register(Vacancy)
admin.site.register(Application)
admin.site.register(Specialty)
admin.site.register(Resume)
