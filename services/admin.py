from django.contrib import admin
from .models import Service,ServiceCategory,ServiceImage


# Register your models here.
class ServiceImageAdminInline(admin.StackedInline):
    model = ServiceImage
    extra = 0


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'service_category', 'create_date', 'update_date')
    search_fields = ('name', 'service_category__name')
    list_filter = ('service_category',)
    date_hierarchy = 'create_date'
    readonly_fields = ('create_date', 'update_date')
    inlines = [ServiceImageAdminInline,]

class ServiceImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ServiceImage._meta.fields]
    list_filter = [field.name for field in ServiceImage._meta.fields]



class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'create_date', 'update_date')
    search_fields = ('name',)







admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(ServiceImage, ServiceImageAdmin)
