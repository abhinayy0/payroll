from rest_framework import serializers
from .models import Employee, Salary

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        read_only_fields = ['id']
        depth = 1
        

class SalarySlipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        depth = 1
        fields =  ['monthly_ctc', 'basic', 'hra', 'ltc', 'other_allowance', 'gross_earnings', 'tds', 'food_meal', 'leave_deduction', 'gross_deductions', 'net_pay', 'fixed_annual_ctc', 'emp_id', 'objects']