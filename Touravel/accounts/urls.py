from django.urls import path
from . import views

app_name = "accounts"


urlpatterns = [
    path("login/", views.login_user, name="login_user"),
    path("register/", views.register_user, name="register_user"),
    path("guide/register/", views.guide_register_user, name="guide_register"),
    path("logout/", views.logout_user, name="logout_user"),

]