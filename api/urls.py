from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('employees', views.EmployeeViewset, basename='employeedirectories')

urlpatterns = [
  path('students/', views.students),
  path('students/<int:pk>/', views.studentDetails),

  #employee urls
  path('employees/', views.Employees.as_view()),
  path('employees/<int:pk>/', views.EmployeeDetails.as_view())
]
