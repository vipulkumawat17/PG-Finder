from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('addpg/',PgView.as_view(),name='addpg'),
    path('addpgdetail/',PgDetailView.as_view(),name='addpgdetail'),
    path('ownerdashboard/',PgListView.as_view(),name='ownerdashboard'),
    path('updatepg/<int:pk>',PgUpdateView.as_view(),name='updatepg'),
    path('deletepg/',PgDeleteView.as_view(),name='deletepg'),
    path('getpgdetails/<int:pk>',PgGetDetailsView.as_view(),name='getpgdetails'),
    path('updatepgdetails/',PgDetailsUpdateView.as_view(),name='updatepgdetails')
]