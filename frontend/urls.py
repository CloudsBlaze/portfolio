from django.urls import path
from frontend.views import (
    HomeIndex,
    ContactUsIndex,
    ServiceIndex,
    AboutIndex,
#    APIIndex
)

urlpatterns = [
    path("", HomeIndex.as_view()),
    path("contact-us", ContactUsIndex.as_view()),
    path("services", ServiceIndex.as_view()),
    path("about-us", AboutIndex.as_view()),
    # path("api", APIIndex.as_view()),
    # path("contact-us/<str:pk>", ContactUsView.as_view()),
]