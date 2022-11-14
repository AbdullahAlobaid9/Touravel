from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .models import Profile

# Create your views here.

def register_user(request: HttpRequest):

    if request.method == "POST":
        new_user = User.objects.create_user(username = request.POST["username"], first_name= request.POST["first_name"], last_name= request.POST["last_name"], email=request.POST["email"], password= request.POST["password"])
        new_user.save()


    return render(request, "accounts/register.html")


def login_user(requset: HttpRequest):
    msg = ""
    
    if requset.method == "POST":
        user = authenticate(requset, username = requset.POST["username"], password = requset.POST["password"])

        if user:
            login(requset, user)
            return redirect("tourApp:home_page")
        else:
            msg = "User Not Found, Try again!"
    
    return render(requset, "accounts/login.html", {"msg": msg})


def logout_user(request: HttpRequest):

    logout(request)

    return redirect("tourApp:home_page")