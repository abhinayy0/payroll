from unicodedata import name
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from employee.models import Designation, Department, Salary, Employee
from datetime import datetime, date

class EmployeeTests(APITestCase):
    def setUp(self):
        self.dept = Department.objects.create(name="Operations")
        self.designation = Designation.objects.create(role="Analyst")

        self.employee_data = {
            "name": 'E1',
            "emp_code":"E001",
            'date_of_birth': date.today(),
            'date_of_joining': date.today(),
            'designation': self.designation,
            'dept': self.dept,
            "bank_ac_no":"123456",
            "pf_no":"EMP2016123",
        }
        self.employee_data_dummy = {
            "name": 'E2',
            "emp_code":"E002",
            'date_of_birth': date.today(),
            'date_of_joining': date.today(),
            'designation': 1,
            'dept': 1,
            "bank_ac_no":"1234563",
            "pf_no":"EMP20161234",
        }


        self.sample_emp = Employee.objects.create(**self.employee_data)
    
    def test_add_employee(self):
        url = reverse('employee:employee')
        response = self.client.post(url, self.employee_data_dummy, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_fail_add_employee(self):
        url = reverse('employee:employee')
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_employee_detail(self):
        url = reverse("employee:employee-detail",  kwargs={'pk': self.sample_emp.id})


    def test_salary_view(self):
        url = reverse("employee:employee-salary",  kwargs={'pk': self.sample_emp.id})