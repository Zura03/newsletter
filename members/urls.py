
from django.urls import path

import letter
from . import views
from letter import views as letter_views
urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('mail_letter/', letter_views.mail_letter, name='mail-letter'),
    path('', letter_views.index, name='letter-index'),
    path('logout_user', views.logout_user, name='logout'),
]