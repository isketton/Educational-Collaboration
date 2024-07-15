from rest_framework import serializers
from .models import *

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parents
        fields = '__all__'
      
class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcements
        fields = '__all__'
        
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'
        
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
        
class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignments
        fields = '__all__'

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clubs
        fields = '__all__'
        
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'
        
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schools
        fields = '__all__'