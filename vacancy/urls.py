from django.urls import path

from vacancy.views import main_view

urlpatterns = [
    path('', main_view, name='main'),
]
