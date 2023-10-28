from django.urls import path
from .views import ContactUsAPI






urlpatterns =[
    path("contact_us/", ContactUsAPI.as_view()),
    path("contact_us/<int:pk>/", ContactUsAPI.as_view())
]