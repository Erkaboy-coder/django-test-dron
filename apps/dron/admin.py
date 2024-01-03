from django.contrib import admin
from apps.dron.models import *

class DronCategoryModelAdmin(admin.ModelAdmin):
    list_display = ["id","name","weight_limit","created_at"]
    list_display_links = ['id', 'name']
admin.site.register(DronCategoryModel, DronCategoryModelAdmin)

admin.site.register(DronModel),
admin.site.register(DeliveryModel)
admin.site.register(MedicationModel)