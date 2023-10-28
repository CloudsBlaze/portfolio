from rest_framework import serializers
from .models import EventImage



class EventImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventImage
        fields = "__all__"