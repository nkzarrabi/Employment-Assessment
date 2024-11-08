from django.urls import path
from . import views

urlpatterns = [
    path('', views.hr_dashboard, name='hr_dashboard'),
    path('roles/', views.role_list, name='role_list'),
    path('roles/add/', views.role_create, name='role_create'),
    path('roles/<int:pk>/edit/', views.role_update, name='role_update'),
    path('roles/<int:pk>/delete/', views.role_delete, name='role_delete'),
    path('criteria/', views.criteria_list, name='criteria_list'),
    path('criteria/add/', views.criteria_create, name='criteria_create'),
    path('criteria/<int:pk>/edit/', views.criteria_update, name='criteria_update'),
    path('criteria/<int:pk>/delete/', views.criteria_delete, name='criteria_delete'),
    path('linked_assessments/', views.linked_assessment_list, name='linked_assessment_list'),
    path('linked_assessments/add/', views.linked_assessment_create, name='linked_assessment_create'),
    path('linked_assessments/<int:pk>/edit/', views.linked_assessment_update, name='linked_assessment_update'),
    path('linked_assessments/<int:pk>/delete/', views.linked_assessment_delete, name='linked_assessment_delete'),
    path('api/criteria/', views.criteria_data, name='criteria_data'),
    path('hr_interface/', views.hr_interface, name='hr_interface'),
]
