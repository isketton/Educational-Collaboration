from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.

class StaffListCreate(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    
    def delete(self, request, *args, **kwargs):
        Staff.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class StaffRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = Staff.objects.all()
  serializer_class = StaffSerializer
  lookup_field = "pk"
  
class StudentListCreate(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    
    def delete(self, request, *args, **kwargs):
        Students.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class StudentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = Students.objects.all()
  serializer_class = StudentSerializer
  lookup_field = "pk"

class ParentListCreate(generics.ListCreateAPIView):
    queryset = Parents.objects.all()
    serializer_class = ParentSerializer
    
    def delete(self, request, *args, **kwargs):
        Parents.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ParentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = Parents.objects.all()
  serializer_class = ParentSerializer
  lookup_field = "pk"
  
class AnnouncementListCreate(generics.ListCreateAPIView):
    queryset = Announcements.objects.all()
    serializer_class = AnnouncementSerializer
    
    def delete(self, request, *args, **kwargs):
        Announcements.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class AnnouncementRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = Announcements.objects.all()
  serializer_class = AnnouncementSerializer
  lookup_field = "pk"

class EventListCreate(generics.ListCreateAPIView):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    
    def delete(self, request, *args, **kwargs):
        Events.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class EventRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = Events.objects.all()
  serializer_class = EventSerializer
  lookup_field = "pk"
  
class ReportListCreate(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    
    def delete(self, request, *args, **kwargs):
        Report.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ReportRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = Report.objects.all()
  serializer_class = ReportSerializer
  lookup_field = "pk"
  
class AssignmentListCreate(generics.ListCreateAPIView):
    queryset = Assignments.objects.all()
    serializer_class = AssignmentSerializer
    
    def delete(self, request, *args, **kwargs):
        Assignments.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class AssignmentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = Assignments.objects.all()
  serializer_class = AssignmentSerializer
  lookup_field = "pk"
  
class ClubListCreate(generics.ListCreateAPIView):
    queryset = Clubs.objects.all()
    serializer_class = ClubSerializer
    
    def delete(self, request, *args, **kwargs):
        Clubs.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ClubRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = Clubs.objects.all()
  serializer_class = ClubSerializer
  lookup_field = "pk"
  
class MessageListCreate(generics.ListCreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer
    
    def delete(self, request, *args, **kwargs):
        Messages.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class MessageRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = Messages.objects.all()
  serializer_class = MessageSerializer
  lookup_field = "pk"
  
class SchoolListCreate(generics.ListCreateAPIView):
    queryset = Schools.objects.all()
    serializer_class = SchoolSerializer
    
    def delete(self, request, *args, **kwargs):
        Schools.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class SchoolRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = Schools.objects.all()
  serializer_class = SchoolSerializer
  lookup_field = "pk"
  
def chat(request):
    return render(request, "chat.html")
  
def room(request, room_name):
    return render(request, "room.html", {"room_name": room_name})