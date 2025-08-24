from django.urls import path
from . import views

urlpatterns = [
    path('biblework/home', views.home, name='bibelwork_home'),
    path('add_study/', views.study_schedule_list, name='add_study'),
    path('add_material/', views.lesson_material_list, name='add_material'),
    path('add_team_member/', views.outreach_team_list, name='add_team_member'),
    path('add_visit/', views.visit_log_list, name='add_visit'),
]
