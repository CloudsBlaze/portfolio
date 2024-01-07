from django.urls import path
from frontend.views import (
    HomeIndex,
    ContactUsIndex,
    ServiceIndex,
    ServiceDetailPage,
    BlogDetailPage,
    AboutIndex,
    thank_you,
    #    APIIndex
)

urlpatterns = [
    path("", HomeIndex.as_view(), name="home"),
    path("contact-us", ContactUsIndex.as_view(), name="contact_us"),
    path("services", ServiceIndex.as_view(), name="service"),
    path(
        "services/<str:title_slug>", ServiceDetailPage.as_view(), name="service_detail"
    ),
    path("blog/<str:title_slug>", BlogDetailPage.as_view(), name="blog_detail"),
    path("about-us", AboutIndex.as_view(), name="aboutus"),
    path("thank-you/", thank_you, name="thank-you-page")
    # path("api", APIIndex.as_view()),
    # path("contact-us/<str:pk>", ContactUsView.as_view()),
]
