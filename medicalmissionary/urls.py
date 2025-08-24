from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='medical_dashboard'),
    path('clinic_schedule/', views.clinic_schedule_list, name='clinic_schedule_list'),
    path('patients/', views.patient_list, name='patient_list'),
    path('volunteers/', views.volunteer_list, name='volunteer_list'),
    path('treatments/', views.treatment_list, name='treatment_list'),
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('health_education/', views.health_education_list, name='health_education_list'),
]
