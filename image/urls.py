from django.urls import path
from .views import  EventImageAPI






urlpatterns =[
    path("image/", EventImageAPI.as_view()),
    path("image/<int:pk>/", EventImageAPI.as_view())
]