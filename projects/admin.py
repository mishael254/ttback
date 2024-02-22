from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import *
class PartnerAdmin(ImportExportModelAdmin):
    list_display = ('organizationName',)
    list_display_links=('organizationName',)

admin.site.register(Partner, PartnerAdmin)

class ProjectCategoryAdmin(ImportExportModelAdmin):
    list_display = ('projectcategoryName',)
    list_display_links=('projectcategoryName',)

admin.site.register(ProjectCategory, ProjectCategoryAdmin)

class ProjectSubCategoryAdmin(ImportExportModelAdmin):
    list_display = ('projectCategory','projectSubcategoryName',)
    list_display_links=('projectCategory',)
    search_fields =('projectCategory','projectSubcategoryName')
    list_filter = ('projectCategory',)

admin.site.register(ProjectSubCategory, ProjectSubCategoryAdmin)

class CountyAdmin(ImportExportModelAdmin):
    list_display = ('country','countyName',)
    list_display_links=('countyName',)
    search_fields =('country','countyName',)
    list_filter = ('country','countyName',)
    

admin.site.register(County, CountyAdmin)

class CountryAdmin(ImportExportModelAdmin):
    list_display = ('countryName',)
    list_display_links=('countryName',)

admin.site.register(Country, CountryAdmin)

class ProjectAdmin(ImportExportModelAdmin):
    list_display = ('projectName','partner','projectCategory','projectCountry','projectCounty','projectZone','projectGroupNo','projectStartDate','projectEndDate')
    list_display_links=('projectName',)
    search_fields =('projectName','partner',)
    list_filter = ('projectCategory','projectCountry','projectCounty','partner')
    

admin.site.register(Project, ProjectAdmin)

class ProjectOfficerAdmin(ImportExportModelAdmin):
    list_display = ('user','project')
    list_display_links=('user',)
    search_fields =('project',)
    list_filter = ('project',)

admin.site.register(ProjectOfficer, ProjectOfficerAdmin)


class LanguageAdmin(ImportExportModelAdmin):
    list_display = ('languageName',)
    list_display_links=('languageName',)

admin.site.register(Language, LanguageAdmin)

class GroupAdmin(ImportExportModelAdmin):
    list_display = ('groupName','project','language')
    list_display_links=('groupName',)
    search_fields =('project','language')
    list_filter = ('project',)

admin.site.register(Group, GroupAdmin)

class MemberAdmin(ImportExportModelAdmin):
    list_display = ('group','membersFirstName','membersLastName','membersEmail','membersPhone','memberGender','memberAge','memberOccupation','memberCategory')
    list_display_links=('group',)
    search_fields =('group','memberGender','memberCategory')
    list_filter = ('group','memberGender','memberCategory')

admin.site.register(Member, MemberAdmin)

class GroupLeaderAdmin(ImportExportModelAdmin):
    list_display = ('member','group','latitude','longitude')
    list_display_links=('member',)
    search_fields =('group',)
    list_filter = ('group',)

admin.site.register(GroupLeader, GroupLeaderAdmin)

