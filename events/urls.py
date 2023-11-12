from django.urls import path
from .views import EventAPI,ParticipantAPI,EventImageAPI






urlpatterns =[
    path("events/", EventAPI.as_view()),
    path("events/<int:pk>/", EventAPI.as_view()),
    path("participant/", ParticipantAPI.as_view()),
    path("participant/<int:pk>/", ParticipantAPI.as_view()),
    path("event-images/", EventImageAPI.as_view()),
    path("event-images/<int:pk>/", EventImageAPI.as_view()),
]