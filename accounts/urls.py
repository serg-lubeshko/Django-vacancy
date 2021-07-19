from django.urls import path

from accounts.views import user_login, register

urlpatterns = [
    path('user_login/', user_login, name='login'),
    path('register/', register, name='register'),
]
