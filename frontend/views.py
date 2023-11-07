from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
# from .serializers import (
#     ContactUsSerializer,
# )
from rest_framework import status
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from django.views.generic.list import ListView

# Create your views here.


class MainView(APIView):

    # def get(self, request, pk=None, format=None):
    #     course_raw =  courses_models.Course.objects.all()
    #     courses = courses_serializers.CourseSerializer(course_raw, many=True)

    #     events_raw =  events_models.Event.objects.all()
    #     events = events_serializers.EventSerializer(events_raw, many=True)

    #     clients_raw =  clients_models.Clients.objects.all()
    #     clients = clients_serializers.ClientsSerializer(clients_raw, many=True)


    #     course_catagoery_raw =  courses_models.CourseCategory.objects.all()
    #     course_catagoery = courses_serializers.CourseCategorySerializer(course_catagoery_raw, many=True)

    #     context = {}
    #     context['courses'] = courses.data
    #     context["events"] = events.data
    #     context["clients"] = clients.data
    #     context["course_catagoery"] = course_catagoery.data

    #     return context

    pass


class HomeIndex(MainView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = './frontend/index.html'

    def get(self, request, pk=None, format=None):
        # main = MainView()
        # context = main.get(request, pk=None, format=None)
        # print(context)

        return Response({"stauts": "success", "data": "context"}, status=status.HTTP_200_OK)

class ContactUsIndex(MainView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = './contact_us/index.html'

    def get(self, request, pk=None, format=None):
        # main = MainView()
        # context = main.get(request, pk=None, format=None)
        # print(context)

        return Response({"stauts": "success", "data": "context"}, status=status.HTTP_200_OK)


class ServiceIndex(MainView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = './services/index.html'

    def get(self, request, pk=None, format=None):
        # main = MainView()
        # context = main.get(request, pk=None, format=None)
        # print(context)

        return Response({"stauts": "success", "data": "context"}, status=status.HTTP_200_OK)

class AboutIndex(MainView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = './about_us/index.html'

    def get(self, request, pk=None, format=None):
        # main = MainView()
        # context = main.get(request, pk=None, format=None)
        # print(context)

        return Response({"stauts": "success", "data": "context"}, status=status.HTTP_200_OK)