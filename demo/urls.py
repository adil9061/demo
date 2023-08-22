from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('forget-password/', forgetpassword, name='forget_password'),
    path('change-password/<token>/', changepassword, name='change_password'),
    path('logout/', logout_view, name='logout'),
]
