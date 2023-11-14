from django.urls import path
from frontend.views import (
    HomeIndex,
    ContactUsIndex,
    ServiceIndex,
    AboutIndex,
    thank_you
#    APIIndex
)

urlpatterns = [
    path("", HomeIndex.as_view(), name="home"),
    path("contact-us", ContactUsIndex.as_view(), name="contact-submit"),
    path("services", ServiceIndex.as_view(), name="service"),
    path("about-us", AboutIndex.as_view(), name="aboutus"),
    path('thank-you/', thank_you, name='thank-you-page')
    # path("api", APIIndex.as_view()),
    # path("contact-us/<str:pk>", ContactUsView.as_view()),
]