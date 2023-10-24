# from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# from .models import ContactUs
# from .serializers import ContactUsSerializer

import contact_us.models as models
import contact_us.serializers as serializers

# Create your views here.
class ContactUsAPI(APIView):
    def get(self, request,  pk=None, format=None):
        if pk is None:
            instance = models.ContactUs.objects.all()
            serializer = serializers.ContactUsSerializer(instance, many=True)
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
                
        instance = get_object_or_404(models.ContactUs, id=pk)
        serializer = serializers.ContactUsSerializer(instance)
        return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
    
    def post(self, request, pk=None, format=None):
        serializer = serializers.ContactUsSerializer(data=request.data)
        print("serializer.is_valid()", serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(

            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    def patch(self, request, pk, format=None):
        instance = models.ContactUs.objects.get(pk=pk)
        serializer = serializers.ContactUsSerializer(
            instance=instance, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    def put(self, request, pk, format=None):
        instance = models.ContactUs.objects.get(pk=pk)
        serializer = serializers.ContactUsSerializer(
            instance=instance, data=request.data, partial=False
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk=None, format=None):
        instance = get_object_or_404(models.ContactUs, pk=pk)
        instance.delete()
        return Response(
            {"msg": "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )


