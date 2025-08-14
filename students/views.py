from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def studenst(request):
  students = [
    {"id": 1, "name": "keshav", "class": "Computer Science and engineering"}
  ]
  return HttpResponse(students)