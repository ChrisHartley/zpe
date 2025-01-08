from django.contrib.gis import admin

# Register your models here.
from .models import planning_case, area_of_interest

class planning_caseAdmin(admin.GISModelAdmin):
    list_display = ['case_date', 'case_number', 'parcel_number', 'description']
    order_by = ['case_date',]

class area_of_interestAdmin(admin.GISModelAdmin):
#    raw_id_fields = ["planning_cases"]
#    readonly_fields = ["planning_cases"]
    pass

admin.site.register(planning_case, planning_caseAdmin)
admin.site.register(area_of_interest, area_of_interestAdmin)
