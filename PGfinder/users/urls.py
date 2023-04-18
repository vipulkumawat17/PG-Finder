from django.contrib import admin
from django.urls import path,include
from users import views
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('ownerregister/',OwnerRegisterView.as_view(),name='ownerregister'),
    path('renderregister/',RenderRegisterView.as_view(),name='renderregister'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('aboutus/',views.AboutUs),
    path('contactus/',views.ContactUs),
    path('service/',views.Service),
    path('logout/',LogoutView.as_view(),name='logout')
    
]