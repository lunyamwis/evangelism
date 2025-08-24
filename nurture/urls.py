from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='nurture_dashboard'),
    path('church-members/', views.church_member_list, name='church_member_list'),
    path('baptized-members/', views.baptized_member_list, name='baptized_member_list'),
    path('baptized-members/<int:member_id>/followups/', views.followup_list, name='followup_list'),
    path('baptized-members/<int:member_id>/followups/add/', views.followup_add, name='followup_add'),
]
