from django.urls import path
from . import views


app_name = "tourApp"


urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("book/tour/", views.book_tour, name="book_tour"),
    path("contact/", views.contact_page, name="contact_page"),
    path("about/", views.about_page, name="about_page"),
    path("profile/guide", views.guide_profile, name="guide_profile"),
    #path("profile/tourist", views.tourist_profile, name="tourist_profile"),
    path("place/add/", views.add_place, name="add_place"),
    path("view/places", views.view_places, name="view_places"),
    path("place/detail/<place_id>/", views.place_detail, name="place_detail"),
    path("place/<place_id>/review/new", views.add_review, name="add_review"),
    path("place/delete/<place_id>", views.delete_place, name="delete_place")
]