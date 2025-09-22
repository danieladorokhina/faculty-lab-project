from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('programs/', views.program_list_view, name='program-list'),
    path('programs/<int:pk>/', views.program_detail_view, name='program-detail'),
    path('departments/', views.department_list_view, name='department-list'),
    path('departments/<int:pk>/', views.department_detail_view, name='department_detail'),
]