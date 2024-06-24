from django.urls import path
from . import views

app_name  = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us/', views.about_us, name='about_us'),
    path('company-services/', views.company_services, name='company_services'),
    path('send-message/', views.send_message, name='send_message'),
]
