from django.contrib import admin
from .models import Employee, Salary, Department, Designation, EmployeeLeaves

# Register your models here.

admin.site.register(Employee)
admin.site.register(Salary)
admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(EmployeeLeaves)