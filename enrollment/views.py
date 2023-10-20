from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic

from .models import Enrollment


class IndexView(generic.ListView):
    model = Enrollment

    # # default -> enrollment/enrollment_list.html
    # template_name = "enrollment/index.html"

    # # default -> "object_list"
    # context_object_name = "enrollments"
