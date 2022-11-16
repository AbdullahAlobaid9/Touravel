from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Place, Review
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def home_page(request : HttpRequest):


    return render(request, "tour/home_page.html")

def login_page(request: HttpRequest):

    return render (request, "tour/login.html")

def register_page(request: HttpRequest):

    return render(request, "tour/register.html")

def guide_register_page(request: HttpRequest):

    return render(request, "tour/guide_register.html")

def contact_page(request: HttpRequest):

    return render(request, "tour/contact.html")

def about_page(request: HttpRequest):

    return render(request, "tour/about.html")


def guide_profile(request: HttpRequest):
    
    return render(request, "tour/guide_profile.html")

def book_tour(request:HttpRequest):

    return render( request, "tour/book_tour.html")



def add_place(request: HttpRequest):
    user: User = request.user

    if not ( user.is_authenticated ) :
        return redirect("accounts:login_user")
    
    if request.method == "POST":
        new_place = Place(user = request.user, place_name= request.POST["place_name"],description = request.POST["description"], image = request.FILES["image"], city = request.POST["city"])
        new_place.save()
        return redirect("tourApp:view_places")
    return render(request, "tour/add_place.html", {"place": Place})

def view_places(request: HttpRequest):

    places = Place.objects.all()

    return render(request, "tour/view_places.html", {"places": places})


def place_detail(request:HttpRequest, place_id: int):

    try:
        place = Place.objects.get(id = place_id)
        reviews = Review.objects.filter(place = place)
    except:
        return render(request, "tour/not_found.html")

    return render(request, "tour/place_detail.html", {"place": place, "review": reviews})


def add_review(request: HttpRequest, place_id : int):
    place = Place.objects.get(id= place_id)

    if request.method == "POST":
        new_review = Review(place = place, name = request.POST["name"],content=request.POST["content"])
        new_review.save()

    return redirect("tourApp:place_detail", place.id)

def delete_place(request: HttpRequest, place_id):
    
    try:
        place = Place.objects.get(id = place_id)
    except:
        return render(request, "tour/not_found.html")
    
    place.delete()

    return redirect("tourApp:view_places")



