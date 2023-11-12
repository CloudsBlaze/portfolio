from rest_framework import serializers
from .models import Service, ServiceCategory

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    service_category = ServiceCategorySerializer()

    class Meta:
        model = Service
        fields = "__all__"

    def create(self, validated_data):
        service_category_data = validated_data.pop('service_category')
        service_category, created = ServiceCategory.objects.get_or_create(name=service_category_data['name'],
            defaults={'description': service_category_data['description']}
        )
        service = Service.objects.create(service_category=service_category, **validated_data)
        return service
    
    def update(self, instance, validated_data):
        service_category_data = validated_data.pop('service_category', None)

        if service_category_data:
            name = service_category_data.get('name')
            description = service_category_data.get('description')
            service_category, created = ServiceCategory.objects.get_or_create(name=name,
            defaults={'description': description})
        
        

            instance.name = validated_data.get('name', instance.name)
            instance.description = validated_data.get('description', instance.description)
            instance.image1 = validated_data.get('image1', instance.image1)
            instance.image2 = validated_data.get('image2', instance.image2)
            instance.service_category = service_category  # Update the service_category
            instance.save()

        return instance
