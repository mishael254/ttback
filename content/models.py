from django.db import models
from projects.models import Project,Language,ProjectCategory,ProjectSubCategory

class Deployment(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    title = models.CharField(max_length=255,verbose_name='Deployment Name')
    deployment = models.IntegerField(verbose_name='Deployment Number')
    deploymentDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ("%s , %s " % (self.title,self.deployment))

class Playlist(models.Model):
    deployment = models.ForeignKey(Deployment,on_delete=models.CASCADE)
    title = models.CharField(max_length=255,verbose_name='Playlist Name Title',default="Lesson 1")
    playlist = models.IntegerField(verbose_name='Playlist Number')
    

    def __str__(self):
        return ("%s , %s " % (self.title,self.deployment))
 
class Message(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE,blank=True,null=True)
    messageTitle = models.CharField(max_length=255)
    messageTopic = models.CharField(max_length=255,blank=True,null=True)
    messageSubTopic = models.CharField(max_length=255,blank=True,null=True)
    messageDescription = models.TextField()
    messageLength = models.IntegerField(verbose_name="Length of message in seconds")
    messageType = models.CharField(max_length=10, choices=[('video', 'Video'), ('audio', 'Audio'), ('image', 'Image')])
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    projectCategory = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    projectSubcategory = models.ForeignKey(ProjectSubCategory, on_delete=models.CASCADE, null=True)
    messagefile = models.URLField(max_length=200,verbose_name="Link To Google Drive Message")
    dateuploaded = models.DateTimeField(auto_now_add=True)
    feedback = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return ("%s , %s , %s" % (self.messageTitle,self.messageTopic,self.dateuploaded))

 

