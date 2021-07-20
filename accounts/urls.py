from django.urls import path

from accounts.views import user_login, register, user_logout

urlpatterns = [
    path('user_login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
]
