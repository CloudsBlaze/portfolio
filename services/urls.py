from django.urls import path
from .views import ServiceAPI, ServiceCategoryAPI, ServiceImageAPI


urlpatterns = [
    path("services/", ServiceAPI.as_view()),
    # path("services/<int:pk>", ServiceAPI.as_view()),
    path("services/<str:title_slug>", ServiceAPI.as_view()),
    path("servicecategory/", ServiceCategoryAPI.as_view()),
    path("servicecategory/<str:title_slug>", ServiceCategoryAPI.as_view()),
    path("serviceimage/", ServiceImageAPI.as_view()),
    path("serviceimage/<int:pk>/", ServiceImageAPI.as_view()),
]
