from django.urls import path

from . import views

urlpatterns = [
    path('insta/', views.index),
    path("upload/", views.upload),
    path("home/", views.album),
    path("photo/<str:category>",views.view_photo,name='view_photo'),
]