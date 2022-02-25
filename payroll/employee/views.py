from datetime import datetime, date
import re
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import EmployeeSerializer, SalarySlipSerializer
from .models import Salary, Employee

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EmployeeDetailView(APIView):

    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self,request, pk):
        emp_object = self.get_object(pk)
        serializer = EmployeeSerializer(emp_object)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        emp_object = self.get_object(pk)
        emp_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  

    def put(self, request, pk):
        emp_object = self.get_object(pk)
        serializer = EmployeeSerializer(emp_object)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeView(APIView):

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SalaryView(APIView):

    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self,request, pk):
        due_month = int(request.GET.get("month", date.today().month))
        due_year = int(request.GET.get("year", date.today().year))
        due_date = date(year=due_year, month=due_month, day=1)
        try:
            due_date = date(year=due_year, month=due_month, day=1)
        except:
            return Response({"detail":"Please enter a valid due date."},status=status.HTTP_400_BAD_REQUEST)
        salary_slips = Salary.objects.filter(emp_id=pk)
        for salary_data in salary_slips:
            if due_date.year == salary_data.reimbursement_date.year and due_date.month == salary_data.reimbursement_date.month:
                salary = salary_data
                serializer =SalarySlipSerializer(salary)
                return Response(serializer.data)
        return Response({"detail":"Salary slip not available."},status=status.HTTP_400_BAD_REQUEST)