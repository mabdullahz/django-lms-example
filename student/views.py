from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic

from .models import Student

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.core.paginator import Paginator


# @login_required(login_url=reverse_lazy('student:login'))
def index(request):
    if request.user.is_authenticated:
        students = Student.objects.all()
        paginator = Paginator(students, 5)  # Show 25 contacts per page.

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        num_visits = request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits + 1

        return render(request, "student/student_list.html", {
            "object_list": students,
            "session": request.session,
            "page_obj": page_obj,
        })
    return redirect(reverse('student:login'))


class DetailView(LoginRequiredMixin, generic.DetailView):
    login_url = "/s/login/"
    context_object_name = "student"
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
