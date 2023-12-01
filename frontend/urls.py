from django.urls import path
from django.views.generic.base import TemplateView
from frontend.views import (
    HomeIndex,
    ContactUsIndex,
    ServiceIndex,
    AboutIndex,
    thank_you,
    robots_txt
#    APIIndex
)

urlpatterns = [
    path("", HomeIndex.as_view(), name="home"),
    path("contact-us", ContactUsIndex.as_view(), name="contact-submit"),
    path("services", ServiceIndex.as_view(), name="service"),
    path("about-us", AboutIndex.as_view(), name="aboutus"),
    path('thank-you/', thank_you, name='thank-you-page'),
    # path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain"))
    path("robots.txt", robots_txt)
    # path("api", APIIndex.as_view()),
    # path("contact-us/<str:pk>", ContactUsView.as_view()),
]