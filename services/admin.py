from django.contrib import admin
from .models import Service,ServiceCategory


# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'service_category', 'create_date', 'update_date')
    search_fields = ('name', 'service_category__name')
    list_filter = ('service_category',)
    date_hierarchy = 'create_date'
    readonly_fields = ('create_date', 'update_date')

class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'create_date', 'update_date')
    search_fields = ('name',)




admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
