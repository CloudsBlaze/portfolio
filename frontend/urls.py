from django.urls import path
from frontend.views import (
    ContactUsIndex,
    HomeIndex,
#     ServicesIndex,
#    AboutIndex,
#    APIIndex
)

urlpatterns = [
    path("", HomeIndex.as_view()),
    # path("services", ServicesIndex.as_view()),
    # path("about-us", AboutIndex.as_view()),
    path("contact-us", ContactUsIndex.as_view()),
    # path("api", APIIndex.as_view()),
    # path("contact-us/<str:pk>", ContactUsView.as_view()),
]