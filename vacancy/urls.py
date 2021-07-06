from django.urls import path

from vacancy.views import main_view, show_list_all_vacancies, show_list_specialty_vacancies

urlpatterns = [
    path('', main_view, name='main'),
    path('vacancies/cat/<str:vacancy>/', show_list_specialty_vacancies, name='specialty_vacancies'),
    path('vacancies/', show_list_all_vacancies, name='list_vacancies'),

]
