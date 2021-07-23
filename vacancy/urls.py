from django.urls import path

from vacancy.views import main_view, show_list_all_vacancies, show_list_specialty_vacancies, \
    card_company_view, vacancy_view, sent, Mycompany, CompanyCreate, CompanyLetsStart, VacancyListCompany

urlpatterns = [
    path('', main_view, name='home'),
    path('vacancies/', show_list_all_vacancies, name='list_vacancies'),
    path('vacancies/cat/<str:specialty>/', show_list_specialty_vacancies, name='specialty_vacancies'),
    path('companies/<int:pk>', card_company_view, name='company_view'),
    path('vacancies/<int:pk>', vacancy_view, name='vacancy_view'),
    path('sent/', sent, name="sent"),
    path('mycompany/',Mycompany.as_view(), name='mycompany'),
    path('mycompany/letsstart/',CompanyLetsStart.as_view(), name='letsstart'),
    path('mycompany/create/',CompanyCreate.as_view(), name='companycreate'),
    path('mycompany/vacancies',VacancyListCompany.as_view(), name='company_vacancies')


]
