from unicodedata import decimal
from django.db import models

# Create your models here.

DEFAULT_DEPT_ID = 1
DEFAULT_DESIG_ID = 1

class Department(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField("dept_name", max_length=30)

    def __str__(self):
        return f"{self.name}"

class Designation(models.Model):
    id = models.BigAutoField(primary_key=True)
    role = models.CharField("role", max_length=30)
    def __str__(self):
        return f"{self.role}"

class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    emp_code =models.CharField(unique=True, null=False, max_length=10)
    name = models.CharField("employee_name", max_length=30)
    date_of_birth=models.DateField(null=False)
    date_of_joining=models.DateField(null=False)
    designation=models.ForeignKey(Designation,  default= DEFAULT_DESIG_ID,on_delete=models.SET_DEFAULT)
    dept=models.ForeignKey(Department, default= DEFAULT_DEPT_ID,on_delete=models.SET_DEFAULT)
    bank_ac_no=models.BigIntegerField(null=False, unique=True)
    pf_no=models.CharField(null=True, max_length=40, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"


class EmployeeLeaves(models.Model):
    id = models.AutoField(primary_key=True)
    working_days = models.IntegerField(null=False, default=22)
    total_leaves = models.IntegerField(null=False, default=22)
    balance_leaves = models.IntegerField(null=False)
    emp_id = models.OneToOneField(Employee, on_delete=models.CASCADE)

    def apply_leave(self, number_of_days):
        if self.balance_leaves - number_of_days > 0:
            self.balance_leaves =  self.balance_leaves - number_of_days
        else: self.balance_leaves = 0
        self.working_days = self.working_days - number_of_days

    @property
    def penalty(self):
        days = self.working_days - 22
        if self.balance_leaves >= 0:
            days = 0
        return days*-1 if days < 0 else 0

class Salary(models.Model):
    id = models.BigAutoField(primary_key=True)
    fixed_annual_ctc= models.FloatField(null=False)
    reimbursement_date = models.DateField()
    emp_id = models.ForeignKey(Employee, on_delete=models.PROTECT)

    @property
    def monthly_ctc(self):
        return round(self.fixed_annual_ctc/12,2)
    
    @property
    def basic(self):
        return round(self.monthly_ctc * .25, 2)
    @property
    def hra(self):
        return round(self.monthly_ctc * .4, 2)
    
    @property
    def ltc(self):
        return round(self.monthly_ctc * 1, 2)
    @property
    def other_allowance(self):
        return round(4500/12, 2)
    
    @property
    def gross_earnings(self):
        return round(self.basic + self.hra + self.ltc + self.other_allowance, 2)
    
    @property
    def tds(self):
        return round(self.monthly_ctc * .10, 2)
    
    @property
    def food_meal(self):
        return round(2500/12, 2)

    @property
    def leave_deduction(self):
        return round(EmployeeLeaves.objects.filter(emp_id=1)[0].penalty * self.monthly_ctc/30, 2)
        
    @property
    def gross_deductions(self):
        return round(self.food_meal + self.tds + self.leave_deduction, 2)

    @property
    def net_pay(self):
        return round(self.gross_earnings - self.gross_deductions, 2)