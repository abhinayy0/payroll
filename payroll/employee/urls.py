from django.urls import path
from employee import views

app_name= "employee"
urlpatterns = [
    path('emp/<int:pk>/', views.EmployeeDetailView.as_view(), name="employee-detail"),
    path('emp/', views.EmployeeView.as_view(), name="employee"),
    path('emp/<int:pk>/salary', views.SalaryView.as_view(), name="employee-salary")
]