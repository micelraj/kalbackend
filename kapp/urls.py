from django.urls import path

from kapp import views

urlpatterns = [
    path('', views.home, name='my home'),
    path('contact/', views.contact, name='contact'),
    path('employee/', views.employee, name='employee_list'),
]

