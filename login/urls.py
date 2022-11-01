from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from .views import LoginViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('login', LoginViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("guidance/", views.guidance, name="guidance"),
    path("research/", views.research, name="research"),
    path("research_1/", views.research_1, name="research_1"),
    path("research_2/", views.research_2, name="research_2"),
    path("research_3/", views.research_3, name="research_3"),
    path("about/", views.about, name="about"),
    path("law_1/", views.law_1, name="law_1"),
    path("law_2/", views.law_2, name="law_2"),
    path("lawpart2/", views.lawpart2, name="lawpart2"),
    path("law_3/", views.law_3, name="law_3"),
    path("law_4/", views.law_4, name="law_4"),
    path("com_law_1/", views.com_law_1, name="com_law_1"),
    path("com_law_2/", views.com_law_2, name="com_law_2"),
    path("com_law_3/", views.com_law_3, name="com_law_3"),
    path("com_law_4/", views.com_law_4, name="com_law_4"),
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
    path(r'token/obtain', TokenObtainPairView.as_view(), name="obtain_token"),
]
