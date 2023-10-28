from django.contrib import admin
from .models import Event,Participant


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'status_type')
    list_filter = ('status_type', 'create_date')
    search_fields = ('title','organizer')

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('user', 'event')
    list_filter = ('event__title', 'user__username')
    search_fields = ('event__title', 'user__username')
    


# Register your models here.
admin.site.register(Event, EventAdmin)
admin.site.register(Participant, ParticipantAdmin)


