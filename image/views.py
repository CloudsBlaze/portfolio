from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.

import image.models as models
import image.serializers as serializers



class EventImageAPI(APIView):
    def get(self, request,  pk=None, format=None):
        if pk is None:
            instance = models.EventImage.objects.all()
            serializer = serializers.EventImageSerializer(instance, many=True)
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        
        instance = get_object_or_404(models.EventImage, id=pk)
        serializer = serializers.EventImageSerializer(instance)
        return Response(
            {"stauts": "success", "data": serializer.data},
            status=status.HTTP_200_OK,
        )
    
    def post(self, request, pk=None, format=None):
        serializer = serializers.EventImageSerializer(data=request.data)
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
        instance = models.EventImage.objects.get(pk=pk)
        serializer = serializers.EventImageSerializer(
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
        instance = models.EventImage.objects.get(pk=pk)
        serializer = serializers.EventImageSerializer(
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
        instance = get_object_or_404(models.EventImage, pk=pk)
        instance.delete()
        return Response(
            {"msg": "Image deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )
