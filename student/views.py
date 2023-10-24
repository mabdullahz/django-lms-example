from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.views import generic

from .models import Student

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class IndexView(generic.ListView):
    model = Student

    # # default -> student/student_list.html
    # template_name = "student/index.html"

    # # default -> "object_list"
    # context_object_name = "students"


class DetailView(generic.DetailView):
    model = Student


def sign_up(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('student:index')) 
        return render(request, "student/student_signup.html")
    elif request.method == "POST":
        user = User.objects.create_user(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            password=request.POST.get('password'),
        )
        return HttpResponseRedirect(reverse('student:login')) 

def login_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('student:index')) 
        return render(request, "student/student_login.html")
    elif request.method == "POST":
        username = request.POST.get('username') # POST["username"]
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('student:index')) 
        else:
            return render(request, "student/student_login.html", {"login_message": "Username/password is incorrect"})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('student:login')) 
