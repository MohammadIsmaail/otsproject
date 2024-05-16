from django.urls import path
from ots.views import *
app_name='ots'

urlpatterns = [
    path('',welcome ),
    path('new-candidate',candidateRegistrationForm,name='registrationForm'),
    path('store-candidate',candidateRegistration),
    path('login',loginView,name='login'),
    path('home',candidateHome),
    path('test-paper',testPaper),
    path('calculate-result',calculateTestResult),
    path('test-history',testResultHistory),
    path('result',showTestResult),
    path('logout',logoutView),
]