from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views

app_name = "account"
urlpatterns = [
    path("login/",LoginView.as_view(template_name="account/login.html"),name="user_login"),
    path("logout/",LogoutView.as_view(next_page="/account/login"),name="user_logout"),
]