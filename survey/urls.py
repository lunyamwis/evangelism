from django.urls import path
from . import views

urlpatterns = [
    path('', views.survey_list, name='survey_list'),
    path('<int:survey_id>/', views.survey_detail, name='survey_detail'),
    path('create/', views.survey_create, name='survey_create'),
    path('<int:survey_id>/add_questions/', views.survey_add_questions, name='survey_add_questions'),
    path('thankyou/', views.survey_thankyou, name='survey_thankyou'),
]
