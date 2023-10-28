from django.urls import path
from .views import EventAPI,ParticipantAPI






urlpatterns =[
    path("events/", EventAPI.as_view()),
    path("events/<int:pk>/", EventAPI.as_view()),
    path("events/", ParticipantAPI.as_view()),
    path("events/<int:pk>/", ParticipantAPI.as_view())
]