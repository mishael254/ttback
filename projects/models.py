from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as gismodels
from django.contrib.gis.geos import Point
#from content.models import Message

class Partner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="user")
    organizationName = models.CharField(max_length=255,verbose_name="organization")

    def __str__(self):
        return str(self.organizationName)

class ProjectCategory(models.Model):
    projectcategoryName = models.CharField(max_length=80,verbose_name="Project Category")
    
    def __str__(self):
        return str(self.projectcategoryName)

class ProjectSubCategory(models.Model):
    projectCategory = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE,verbose_name="project Category")
    projectSubcategoryName = models.CharField(max_length=80,verbose_name="project Sub category")

    def __str__(self):
        return str(self.projectCategory) +" , " + str(self.projectSubcategoryName) 

class Country(models.Model):
    countryName = models.CharField(max_length=40,default="Kenya",verbose_name="country Name")

    def __str__(self):
        return str(self.countryName)

class County(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    countyName = models.CharField(max_length=30, verbose_name="County")

    def __str__(self):
        return str(self.countyName) + ' , ' + str(self.country)

class Project(models.Model):
    projectName = models.CharField(max_length=80, verbose_name="Project Name")
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE,verbose_name="Partner Name")
    projectCategory = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE,verbose_name="Project Category")
    projectSubcategory = models.ForeignKey(ProjectSubCategory, on_delete=models.CASCADE, null=True,verbose_name="Project Sub Category")
    #Client request but not nes
    levelThreeCategory = models.CharField(max_length=80, blank=True, null=True)
    levelFourCategory = models.CharField(max_length=80, blank=True, null=True)
    levelFiveCategory = models.CharField(max_length=80, blank=True, null=True)
    levelSixCategory = models.CharField(max_length=80, blank=True, null=True)
    #**********************************
    projectCountry = models.ForeignKey(Country, on_delete=models.CASCADE,verbose_name="Country")
    projectCounty = models.ForeignKey(County, on_delete=models.CASCADE, verbose_name="County")
    projectZone = models.CharField(max_length=40,verbose_name="Zone")
    projectStartDate = models.DateField(verbose_name="Start Date")
    projectEndDate = models.DateField(verbose_name="End Date")
    projectGroupNo = models.IntegerField(verbose_name="Group No")
    projectMode = models.CharField(max_length=10,choices=[('Open', 'Open'), ('Modular', 'Modular')],default="Open",verbose_name="Learning Mode")
    #channel = models.ForeignKey(Channel, on_delete=models.CASCADE,blank=True,null=True,verbose_name="Channel")
    grouped = models.BooleanField(default=True)
    projectAnthem =  models.URLField(max_length=200,blank=True,null=True,verbose_name="Anthem")
    projectTheme = models.URLField(max_length=200,blank=True,null=True,verbose_name="Theme")

    def __str__(self):
        return ("%s , %s " %  (self.projectName,self.projectZone))

class ProjectOfficer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="User")
    project = models.ForeignKey(Project, on_delete=models.CASCADE,verbose_name="Project")
    
    def __str__(self):
        return ("%s , %s, %s" %  (self.project, self.user.first_name, self.user.last_name,))
    
class Language(models.Model):
    languageName = models.CharField(max_length=30,verbose_name="Language")
    def __str__(self):
        return str(self.languageName)
    
class Group(models.Model):
    groupName = models.CharField(max_length=40,verbose_name="Group Name")
    #groupChannel = models.ForeignKey(Channel, on_delete=models.SET_NULL, blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,verbose_name="Project")
    language = models.ForeignKey(Language, on_delete=models.CASCADE,verbose_name="Language")
    def __str__(self):
        return ("%s , %s"  % (self.groupName,self.project))
class Member(models.Model):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)
    membersFirstName = models.CharField(max_length=30,verbose_name="First Name")
    membersLastName = models.CharField(max_length=30,verbose_name="Last Name")
    membersEmail = models.EmailField(verbose_name="Email")
    membersPhone = models.CharField(max_length=13,verbose_name="Phone Number")
    memberGender = models.CharField(max_length=6,choices=[('Male', 'Male'), ('Female', 'Female')],verbose_name="Gender")
    memberAge = models.IntegerField(verbose_name="Age")
    memberOccupation = models.CharField(max_length=30,verbose_name="Occupation")
    memberCategory = models.CharField(max_length=6, choices=[('Member', 'Member'), ('Leader', 'Leader')],default="Member",verbose_name="Category")
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    location = gismodels.PointField(blank=True, null=True, srid=4326)

    def __str__(self):
        return ("%s , %s " %  (self.membersFirstName,self.membersLastName))
    def save(self, *args, **kwargs):
        if self.latitude and self.longitude:
            self.location = Point(float(self.longitude), float(self.latitude))
            return super(Member, self).save(*args, **kwargs)
        return super(Member, self).save(*args, **kwargs)

class UngroupedMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE,verbose_name="Language")
    membersFirstName = models.CharField(max_length=30,verbose_name="First Name")
    membersLastName = models.CharField(max_length=30,verbose_name="Last Name")
    membersEmail = models.EmailField(verbose_name="Email")
    membersPhone = models.CharField(max_length=13,verbose_name="Phone Number")
    memberGender = models.CharField(max_length=6,choices=[('Male', 'Male'), ('Female', 'Female')],verbose_name="Gender")
    memberAge = models.IntegerField(verbose_name="Age")
    memberOccupation = models.CharField(max_length=30,verbose_name="Occupation")
    memberCategory = models.CharField(max_length=6, choices=[('Member', 'Member'), ('Leader', 'Leader')],default="Member",verbose_name="Category")
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    location = gismodels.PointField(blank=True, null=True, srid=4326)

    def __str__(self):
        return ("%s , %s " %  (self.membersFirstName,self.membersLastName))
    def save(self, *args, **kwargs):
        if self.latitude and self.longitude:
            self.location = Point(float(self.longitude), float(self.latitude))
            return super(Member, self).save(*args, **kwargs)
        return super(Member, self).save(*args, **kwargs)

class GroupLeader(models.Model):
    member= models.ForeignKey(Member, on_delete=models.CASCADE,verbose_name="Member")
    group = models.ForeignKey(Group, on_delete=models.CASCADE,verbose_name="Group")
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return ("%s , %s " %  (self.member,self.group))
    
# class Channel(models.Model):
#     channelName = models.CharField(max_length=255,verbose_name="Channel Name",default="Nairobi & Environs")
#     CHANNEL_OPTIONS = [
#         (1, 'Channel 1'),
#         (2, 'Channel 2'),
#         (3, 'Channel 3'),
#         (4, 'Channel 4'),
#         (5, 'Channel 5'),
#         (6, 'Channel 6'),
#         (7, 'Channel 7'),
#         (8, 'Channel 8'),
#         (9, 'Channel 9'),
#         (10, 'Channel 10'),
#         (11, 'Channel 11'),
#         (12, 'Channel 12'),
#         (13, 'Channel 13'),
#         (14, 'Channel 14'),
#         (15, 'Channel 15'),
#         (16, 'Channel 16'),
#         (17, 'Channel 17'),
#         (18, 'Channel 18'),
#         (19, 'Channel 19'),
#         (20, 'Channel 20'),
#         (21, 'Channel 21'),
#         (22, 'Channel 22'),
#         (23, 'Channel 23'),
#         (24, 'Channel 24'),
#     ]

#     channel = models.IntegerField(choices=CHANNEL_OPTIONS)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE,verbose_name="Project",blank=True,null=True)
#     message = models.ForeignKey(Message, on_delete=models.CASCADE,blank=True,null=True)
#     latitude = models.CharField(max_length=20, blank=True, null=True)
#     longitude = models.CharField(max_length=20, blank=True, null=True)
#     radius = models.IntegerField(verbose_name="Channel Radius")
#     def __str__(self):
#         return ("%s , %s " %  (self.channel,self.radius))



