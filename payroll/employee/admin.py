from django.contrib import admin
from .models import Employee, Salary, Department, Designation

# Register your models here.

admin.site.register(Employee)
admin.site.register(Salary)
admin.site.register(Department)
admin.site.register(Designation)