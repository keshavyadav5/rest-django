from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def students(request):
  students = {
    'id': 1,
    'name': "abc",
    'course': 'xyz'
  }
  return JsonResponse(students)