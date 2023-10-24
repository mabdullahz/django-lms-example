from django.urls import path

from . import views

app_name = 'student'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>", views.DetailView.as_view(), name="detail"),
    path("signup", views.sign_up, name="sign_up"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
]