from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="LogInPage"),
    path("LogIn", views.handleLogIn, name="handleLogIn"),
    path("LogOut", views.handleLogOut, name="handleLogIn"),
    path("ClientPage/", views.ClientPage, name="ClientPage"),
    path("ServPage/", views.ServPage, name="ServPage"),
    path("ContactUs/", views.ContactUs, name="ContactUs"),
    path("Service", views.Service, name="Service"),
    path("AddService/", views.AddService, name="AddService"),
    path("Contact", views.Contact, name="Contact"),
]
