from django.contrib import admin
from .models import service


class ServiceAdmin(admin.ModelAdmin):
    exclude = ('creater',)
    list_display = ('Service_Name','creater',)
    

    def get_queryset(self, request, *agrs, **kwargs):
        if request.user.is_superuser:
            return service.objects.all()
        else:
            return service.objects.filter(creater=request.user)

    def get_list_display(self, request, *agrs, **kwargs):
        if request.user.is_superuser:
            return('Service_Name','creater',)
        else:
            return('Service_Name',)



    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.creater = request.user
            obj.save()

admin.site.register(service, ServiceAdmin)