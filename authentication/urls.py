from .import views
from django.urls import URLPattern
from django.urls import path

urlpatterns = [ 
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.register, name="register"),
]