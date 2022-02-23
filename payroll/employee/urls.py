from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from employee import views

urlpatterns = [
    path('emp/<int:pk>/', views.EmployeeView.as_view()),
]