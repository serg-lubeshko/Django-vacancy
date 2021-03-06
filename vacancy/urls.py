from django.urls import path

from vacancy.views.my_company import Mycompany, CompanyLetsStart, CompanyCreate
from vacancy.views.my_cv import ResumeEdit, ResumeLetsStart, ResumeCreate
from vacancy.views.my_vacancy import VacancyResponse, sent, VacancyListCompany, VacancyEdit, VacancyCreate, \
    VacancySearch
from vacancy.views.public import main_view, show_list_all_vacancies, show_list_specialty_vacancies, card_company_view

urlpatterns = [
    path('', main_view, name='home'),
    path('vacancies/', show_list_all_vacancies, name='list_vacancies'),
    path('vacancies/cat/<str:specialty>/', show_list_specialty_vacancies, name='specialty_vacancies'),
    path('companies/<int:pk>/', card_company_view, name='company_view'),
    path('vacancies/<int:pk>/', VacancyResponse.as_view(), name='vacancy_view'),
    path('sent/', sent, name="sent"),
    path('mycompany/', Mycompany.as_view(), name='mycompany'),
    path('mycompany/letsstart/', CompanyLetsStart.as_view(), name='letsstart'),
    path('mycompany/create/', CompanyCreate.as_view(), name='companycreate'),
    path('mycompany/vacancies', VacancyListCompany.as_view(), name='company_vacancies'),
    path('mycompany/vacancies/<int:vacancy_id>/', VacancyEdit.as_view(), name='vacancy_edit'),
    path('mycompany/vacancies/create/', VacancyCreate.as_view(), name='vacancy_create'),
    path('vacancies/search/', VacancySearch.as_view(), name='search_vacancies'),
    path('myresume/', ResumeEdit.as_view(), name='resume_edit'),
    path('myresume/letsstart', ResumeLetsStart.as_view(), name='resume_letsstart'),
    path('myresume/create/', ResumeCreate.as_view(), name='resume_create'),

]
