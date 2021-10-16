from django.contrib import admin
from .models import Comment, Lead

# Register your models here.

admin.site.register(Comment)



from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

@admin.register(Lead)
class LeadAdmin(ImportExportModelAdmin):
    pass