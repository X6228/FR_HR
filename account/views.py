from django.shortcuts import render
from .forms import LoginForm


# def user_login(request):
#     if request.method == "GET":
#         login_form = LoginForm()
#         return render(request,"account/login.html",{"form":login_form})
#     if request.method == "POST":
#         login_form = LoginForm(request.POST)
#         if login_form.is_valid():
#             login_data = login_form.cleaned_data
#             user = authenticate(username=login_data["username"],password=login_data["password"])

