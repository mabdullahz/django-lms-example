from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic

from .models import Course


class IndexView(generic.ListView):
    model = Course

    # # default -> course/course_list.html
    # template_name = "course/index.html"

    # # default -> "object_list"
    # context_object_name = "courses"
