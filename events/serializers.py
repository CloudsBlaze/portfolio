from rest_framework import serializers
from .models import Event,Participant



class ParticipantSerializer(serializers.ModelSerializer):
     
     class Meta:
         model = Participant
         fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length=100, required=False)
    # start_date = serializers.DateTimeField(required=False)
    participants =ParticipantSerializer(many=True, read_only=True)  # event has many event_Participants

    class Meta:
         model = Event
         fields = "__all__"

    def create(self, validated_data):
        custom_field = validated_data.pop('custom_field', None)
        event = Event.objects.create(**validated_data)

        if custom_field is not None:

            pass

        return event
    
    def update(self, instance, validated_data):
        
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.status_type = validated_data.get('status_type', instance.status_type)
        instance.organizer = validated_data.get('organizer', instance.organizer)
        instance.save()

        return instance