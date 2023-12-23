from django.urls import path
from contact_us.views import ContactUsAPI


urlpatterns = [
    path("contact-us/", ContactUsAPI.as_view(), name="api-contact-us"),
    path("contact-us/<int:pk>/", ContactUsAPI.as_view(), name="api-contact-us"),
]
