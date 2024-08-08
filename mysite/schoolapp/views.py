from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, authentication, permissions
from rest_framework.settings import api_settings
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.contrib.auth import authenticate
from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication
from rest_framework.authentication import SessionAuthentication

# Create your views here.

class UserListCreate(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
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
'''  
class MessageListCreate(generics.ListCreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer
    
    def delete(self, request, *args, **kwargs):
        Messages.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class MessageRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = Messages.objects.all()
  serializer_class = MessageSerializer
  lookup_field = "pk"'''
  
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
  
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    
class CreateStudentView(generics.CreateAPIView):
    serializer_class = StudentSerializer

class CreateParentView(generics.CreateAPIView):
    serializer_class = ParentSerializer

class CreateStaffView(generics.CreateAPIView):
    serializer_class = StaffSerializer
class LoginView(KnoxLoginView):
    serializer_class = AuthSerializer
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        response =  super(LoginView, self).post(request, format=None)

        token = response.data['token']
        del response.data['token']
        
        response.set_cookie(
            'auth_token',
            token,
            httponly=True,
            samesite='strict'
        )
        return response
      
class ManageUserView(generics.RetrieveUpdateAPIView): 
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_object(self):
        return self.request.user
    
      
  
def chat(request):
    return render(request, "chat.html")
  
def room(request, room_name):
    return render(request, "room.html", {"room_name": room_name})