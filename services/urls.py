from django.urls import path
from .views import ServiceAPI,ServiceCategoryAPI






urlpatterns =[
   
    path("services/", ServiceAPI.as_view()),
    path("services/<int:pk>/", ServiceAPI.as_view()),
    path("servicecategory/", ServiceCategoryAPI.as_view()),
    path("servicecategory/<int:pk>/", ServiceCategoryAPI.as_view())
]