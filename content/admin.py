from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
from api.models import StatLog

class MessageAdmin(ImportExportModelAdmin):
    list_display = ('messageTitle','messageTopic','messageSubTopic','messageDescription','messageLength','messageType','language','projectCategory','projectSubcategory','messagefile','dateuploaded')
    list_display_links=('messageTitle',)
    search_fields =('messageType','language','projectCategory','projectSubcategory')
    list_filter = ('messageType','language','projectCategory','projectSubcategory')

admin.site.register(Message, MessageAdmin)
# class StatLogAdmin(ImportExportModelAdmin):
#     list_display = ('message','member','startTime','endTime','messageLength','messageCompleted','dateloged')
#     list_display_links=('message',)
#     search_fields =('message','member','messageCompleted',)
#     list_filter = ('message','member','messageCompleted',)

# admin.site.register(StatLog, StatLogAdmin)
