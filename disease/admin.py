from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

# Register your models here.
from .models import breastCancer

class breastCancerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...

admin.site.register(breastCancer,breastCancerAdmin)