from django.db import models

# Create your models here.

DEFAULT_DEPT_ID = 1
DEFAULT_DESIG_ID = 1

class Department(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField("dept_name", max_length=30)

class Designation(models.Model):
    id = models.BigAutoField(primary_key=True)
    role = models.CharField("role", max_length=30)

class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    emp_code =models.CharField(unique=True, null=False, max_length=10)
    name = models.CharField("employee_name", max_length=30)
    date_of_birth=models.DateField(null=False)
    date_of_joining=models.DateField(null=False)
    designation=models.OneToOneField(Designation,  default= DEFAULT_DESIG_ID,on_delete=models.SET_DEFAULT)
    dept=models.OneToOneField(Department, default= DEFAULT_DEPT_ID,on_delete=models.SET_DEFAULT)
    bank_ac_no=models.BigIntegerField(null=False)
    pf_no=models.CharField(null=True, max_length=40)


class Salary(models.Model):
    id = models.BigAutoField(primary_key=True)
    fixed_anual_ctc= models.FloatField(null=False)
    balance_leaves = models.IntegerField(null=False)
    emp_id = models.ForeignKey(Employee, on_delete=models.PROTECT)
