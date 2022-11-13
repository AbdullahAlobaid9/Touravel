from django.urls import path
from . import views


app_name = "tourApp"


urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("login/", views.login_page, name="login_page"),
    path("register/", views.register_page, name="register_page"),
    path("guide/register/", views.guide_register_page, name="guide_register_page"),
    path("contact/", views.contact_page, name="contact_page"),
    path("about/", views.about_page, name="about_page")


]