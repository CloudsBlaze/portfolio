from django.contrib import admin
from .models import ContactUs

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'create_date')
    list_filter = ('create_date',)
    search_fields = ('first_name', 'email')

# Register your models here.
admin.site.register(ContactUs, ContactUsAdmin)
