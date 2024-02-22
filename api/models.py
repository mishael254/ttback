from django.db import models

class StatLog(models.Model):
    #for project
    project = models.CharField(max_length=80, blank=True, null=True)
    partner = models.CharField(max_length=80, blank=True, null=True)
    Category = models.CharField(max_length=80, blank=True, null=True)
    Subcategory = models.CharField(max_length=80, blank=True, null=True)
    levelThreeCategory = models.CharField(max_length=80, blank=True, null=True)
    levelFourCategory = models.CharField(max_length=80, blank=True, null=True)
    levelFiveCategory = models.CharField(max_length=80, blank=True, null=True)
    levelSixCategory = models.CharField(max_length=80, blank=True, null=True)
    Country = models.CharField(max_length=80, blank=True, null=True)
    County = models.CharField(max_length=80, blank=True, null=True)
    Zone = models.CharField(max_length=40, blank=True, null=True)
    StartDate = models.DateField(blank=True, null=True)
    EndDate = models.DateField(blank=True, null=True)
    GroupNo = models.IntegerField(blank=True, null=True)
    Mode = models.CharField(max_length=10, blank=True, null=True)
    channel = models.CharField(max_length=14, blank=True, null=True)
    #for message 
    messageTitle = models.CharField(max_length=255, blank=True, null=True)
    Topic = models.CharField(max_length=50, blank=True, null=True)
    SubTopic = models.CharField(max_length=70, blank=True, null=True)
    Length = models.IntegerField(blank=True, null=True)
    Type = models.CharField(max_length=10, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    dateuploaded = models.DateTimeField(auto_now_add=True)
    #member
    group = models.CharField(max_length=20, blank=True, null=True)
    Gender = models.CharField(max_length=6, blank=True, null=True)
    Age = models.CharField(max_length=3, blank=True, null=True)
    Occupation = models.CharField(max_length=20, blank=True, null=True)
    Category = models.CharField(max_length=20, blank=True, null=True)
    latitude = models.CharField(max_length=8, blank=True, null=True)
    longitude = models.CharField(max_length=8, blank=True, null=True)
    
    def __str__(self):
        return ("%s , %s " %  (self.project,self.messageTitle))

class Feedback(models.Model):
    message = models.CharField(max_length=70,blank=True,null=True)
    member = models.CharField(max_length=70,blank=True, null=True)
    feedBack = models.TextField(max_length=700,blank=True, null=True,verbose_name="Feedback Text")
    feedbackTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ("%s , %s" % (self.message,self.member))