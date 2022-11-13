from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def home_page(request : HttpRequest):


    return render(request, "tour/home_page.html")


def login_page(request: HttpRequest):

    return render (request, "tour/login.html")

def register_page(request: HttpRequest):

    return render(request, "tour/register.html")

def guide_register_page(request: HttpRequest):

    return render(request, "tour/guide_register.html")
