from django.contrib import admin

from .models import Company, Vacancy, Application, Specialty, User


admin.site.register(Company)
admin.site.register(Vacancy)
admin.site.register(Application)
admin.site.register(Specialty)
