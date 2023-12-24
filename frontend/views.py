from django.shortcuts import render, redirect
from django.urls import reverse


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
from contact_us.serializers import ContactUsSerializer

import services.models as ServicesModels
import services.serializers as ServicesSerializers

# Create your views here.


class MainView(APIView):
    def get(self, request, pk=None, format=None):
        services_raw = ServicesModels.ServiceCategory.objects.all()
        service_catgories = ServicesSerializers.ServiceCategorySerializer(
            services_raw, many=True
        )

        #     events_raw =  events_models.Event.objects.all()
        #     events = events_serializers.EventSerializer(events_raw, many=True)

        #     clients_raw =  clients_models.Clients.objects.all()
        #     clients = clients_serializers.ClientsSerializer(clients_raw, many=True)

        #     course_catagoery_raw =  courses_models.CourseCategory.objects.all()
        #     course_catagoery = courses_serializers.CourseCategorySerializer(course_catagoery_raw, many=True)

        context = {}
        context["service_catgories"] = service_catgories.data
        #     context["events"] = events.data
        #     context["clients"] = clients.data
        #     context["course_catagoery"] = course_catagoery.data

        return context
        pass


class HomeIndex(MainView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "./frontend/index.html"

    def get(self, request, pk=None, format=None):
        main = MainView()
        context = main.get(request, pk=None, format=None)

        return Response(
            {"stauts": "success", "context": context}, status=status.HTTP_200_OK
        )


class ContactUsIndex(MainView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "./contact_us/index.html"

    def get(self, request, pk=None, format=None):
        main = MainView()
        context = main.get(request, pk=None, format=None)

        return Response(
            {"stauts": "success", "context": context}, status=status.HTTP_200_OK
        )

    def post(self, request, pk=None, format=None):
        print("request.data", request.data)
        serializer = ContactUsSerializer(data=request.data)
        print("serializer.is_valid() running from templates", serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            print("serializer.data", serializer.data)
            # return redirect('thank-you-page')
            request.session["name"] = serializer.data["first_name"]
            request.session[
                "message"
            ] = "Thank you for your kind support and valuable feedback. Your contribution means a lot to us, and it helps us improve our services. We appreciate your trust in us and look forward to serving you in the future."
            return redirect(reverse('thank-you-page'))
        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class ServiceIndex(MainView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "./services/index.html"

    def get(self, request, pk=None, format=None):
        main = MainView()
        context = main.get(request, pk=None, format=None)

        return Response(
            {"stauts": "success", "context": context}, status=status.HTTP_200_OK
        )


class ServiceDetailPage(MainView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "./services/detail.html"

    def get(self, request, pk=None, title_slug=None, format=None):
        main = MainView()
        context = main.get(request, pk=None, format=None)

        if title_slug is not None:
            instance = get_object_or_404(
                ServicesModels.ServiceCategory, service_category_slug=title_slug
            )
            serializer = ServicesSerializers.ServiceCategorySerializer(instance)

            return Response(
                {"stauts": "success", "data": serializer.data, "context": context},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"stauts": "success", "context": context}, status=status.HTTP_200_OK
        )


class AboutIndex(MainView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "./about_us/index.html"

    def get(self, request, pk=None, format=None):
        main = MainView()
        context = main.get(request, pk=None, format=None)

        return Response(
            {"stauts": "success", "data": context}, status=status.HTTP_200_OK
        )


def thank_you(request):
    name = request.session.get("name", "")
    message = request.session.get("message", "")

    context = {
        "name": name,
        "message": message,
    }
    return render(request, "./thanks/thank_you.html", context)
