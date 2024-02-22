from rest_framework import serializers
#from .models import UsageLog, Feedback
from content.models import Deployment, Playlist, Message
from .models import StatLog,Feedback

from projects.models import Project, Member, UngroupedMember

# Serializer for Project (Read-only)
class ProjectNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['projectName']

# Serializer for Member
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

# Serializer for UngroupedMember
class UngroupedMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = UngroupedMember
        fields = '__all__'

class DeploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deployment
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class StatLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatLog
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
