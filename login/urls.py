from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("register/", views.register, name="register"),
    path("search/", views.search, name="search"),
    path("<cid>/category/", views.category, name="category"),
    path("<id>/product/", views.product, name="product"),
    path("contact/", views.contact, name="contact"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="login/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="login/logout.html"),
        name="logout",
    ),
]
