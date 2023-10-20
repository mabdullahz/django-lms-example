from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic

from .models import Student


class IndexView(generic.ListView):
    model = Student

    # # default -> student/student_list.html
    # template_name = "student/index.html"

    # # default -> "object_list"
    # context_object_name = "students"


class DetailView(generic.DetailView):
    model = Student
