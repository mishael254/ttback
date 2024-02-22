from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from api.models import StatLog,Feedback

class StatLogAdmin(ImportExportModelAdmin):
    list_display = [field.attname for field in StatLog._meta.fields]
    list_display_links=()
    search_fields =[field.attname for field in StatLog._meta.fields]
    list_filter = [field.attname for field in StatLog._meta.fields]
admin.site.register(StatLog, StatLogAdmin)

class FeedbackAdmin(ImportExportModelAdmin):
    list_display = [field.attname for field in Feedback._meta.fields]
    list_display_links=()
    search_fields =[field.attname for field in Feedback._meta.fields]
    list_filter = [field.attname for field in Feedback._meta.fields]
admin.site.register(Feedback, FeedbackAdmin)
