from django.contrib import admin
from django.urls import include, path
from .views import *
urlpatterns = [
    path('', ListBooksAPIView.as_view()),
     path('register', RegisterBookAPIView.as_view()),
    path('delete/<str:pk>', DeleteBookAPIView.as_view()),
    path('update/<str:pk>', UpdateBookAPIView.as_view()),
    path('<str:id>',RetrieveBookAPIView.as_view()),
    path('upload', Upload_view.as_view()),
]