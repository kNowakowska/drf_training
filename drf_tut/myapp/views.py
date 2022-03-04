from django.shortcuts import render
from django.http import JsonResponse
from myapp.models import Employee

# Create your views here.


def employee_view(request):
    employees = Employee.objects.all()
    response = {'employees': list(employees.values('name', 'salary'))}

    return JsonResponse(response)
