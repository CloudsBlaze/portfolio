from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

import services.models as models
import services.serializers as serializers

# Create your views here.
class ServiceAPI(APIView):
    def get(self, request,  pk=None, format=None):
        if pk is None:
            instance = models.Service.objects.all()
            serializer = serializers.ServiceSerializer(instance, many=True)
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        
        instance = get_object_or_404(models.Service, id=pk)
        serializer = serializers.ServiceSerializer(instance)
        return Response(
            {"stauts": "success", "data": serializer.data},
            status=status.HTTP_200_OK,
        )
    
    
    def post(self, request, pk=None, format=None):
        serializer = serializers.ServiceSerializer(data=request.data)
        print("serializer.is_valid()", serializer.is_valid())
        if serializer.is_valid():
            serializer.save()

            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        
    def put(self, request, pk, format=None):
        instance = models.Service.objects.get(pk=pk)
        serializer = serializers.ServiceSerializer(
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
        instance = get_object_or_404(models.Service, pk=pk)
        instance.delete()
        return Response(
            {"msg": "service deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )
    
        
    
class ServiceCategoryAPI(APIView):
    def get(self, request,  pk=None, format=None):
        if pk is None:
            instance = models.ServiceCategory.objects.all()
            serializer = serializers.ServiceCategorySerializer(instance, many=True)
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        
        instance = get_object_or_404(models.ServiceCategory, id=pk)
        serializer = serializers.ServiceCategorySerializer(instance)
        return Response(
            {"stauts": "success", "data": serializer.data},
            status=status.HTTP_200_OK,
        )
    
    def post(self, request, pk=None, format=None):
        serializer = serializers.ServiceCategorySerializer(data=request.data)
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
    
    def put(self, request, pk, format=None):
        instance = models.ServiceCategory.objects.get(pk=pk)
        serializer = serializers.ServiceCategorySerializer(
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
        instance = get_object_or_404(models.ServiceCategory, pk=pk)
        instance.delete()
        return Response(
            {"msg": "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )
    

class ServiceImageAPI(APIView):
    def get(self, request,  pk=None, format=None):
        if pk is None:
            instance = models.ServiceImage.objects.all()
            serializer = serializers.ServiceImageSerializer(instance, many=True)
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        
        instance = get_object_or_404(models.ServiceImage, id=pk)
        serializer = serializers.ServiceImageSerializer(instance)
        return Response(
            {"stauts": "success", "data": serializer.data},
            status=status.HTTP_200_OK,
        )
    
    def post(self, request, pk=None, format=None):
        serializer = serializers.ServiceImageSerializer(data=request.data)
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
    
    def put(self, request, pk, format=None):
        instance = models.ServiceImage.objects.get(pk=pk)
        serializer = serializers.ServiceImageSerializer(
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
        instance = get_object_or_404(models.ServiceImage, pk=pk)
        instance.delete()
        return Response(
            {"msg": "Image deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )
