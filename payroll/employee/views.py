from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import EmployeeSerializer, Employee

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EmployeeView(APIView):

    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self,request, pk):
        emp_object = self.get_object(pk)
        serializer = EmployeeSerializer(emp_object)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pass

    def patch(self, request, pk):
        pass

    def get_salary(self):
        pass