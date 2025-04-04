from django.urls import path, re_path
from . import views
from . import chat_handler
from knox import views as knox_views


websocket_urlpatterns = [
    re_path(r"ws/schoolapp/(?P<room_name>\w+)/$", chat_handler.ChatUser.as_asgi()),
]

urlpatterns = [
    path('create/',views.CreateUserView.as_view(), name="create"),
    path('createstudent/', views.CreateStudentView.as_view(), name='creatstudent'),
    path('createstaff/', views.CreateStaffView.as_view(), name='creatstaff'),
    path('createparent/', views.CreateParentView.as_view(), name='creatparent'),
    path('profile/', views.ManageUserView.as_view(), name="profile"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path("staff/", views.StaffListCreate.as_view(), name="staff-view-create"),
    path("staff/<int:pk>/", views.StaffRetrieveUpdateDestroy.as_view(), 
         name="update",),
    path("student/", views.StudentListCreate.as_view(), name="student-view-create"),
    path("student/<int:pk>/", views.StudentRetrieveUpdateDestroy.as_view(), 
         name="update",),
    path("parent/", views.ParentListCreate.as_view(), name="parent-view-create"),
    path("parent/<int:pk>/", views.ParentRetrieveUpdateDestroy.as_view(), 
         name="update",),
    path("announcement/", views.AnnouncementListCreate.as_view(), name="announcement-view-create"),
    path("announcement/<int:pk>/", views.AnnouncementRetrieveUpdateDestroy.as_view(), 
         name="update",),
    path("event/", views.EventListCreate.as_view(), name="event-view-create"),
    path("event/<int:pk>/", views.EventRetrieveUpdateDestroy.as_view(), 
         name="update",),
    path("report/", views.ReportListCreate.as_view(), name="report-view-create"),
    path("reports/<int:pk>/", views.ReportRetrieveUpdateDestroy.as_view(), 
         name="update",),
    path("assignment/", views.AssignmentListCreate.as_view(), name="assignment-view-create"),
    path("assignment/<int:pk>/", views.AssignmentRetrieveUpdateDestroy.as_view(), 
         name="update",),
    path("club/", views.ClubListCreate.as_view(), name="club-view-create"),
    path("club/<int:pk>/", views.ClubRetrieveUpdateDestroy.as_view(), 
         name="update",),
    path("school/", views.SchoolListCreate.as_view(), name="school-view-create"),
    path("school/<int:pk>/", views.SchoolRetrieveUpdateDestroy.as_view(), 
         name="update",),
    
    path("", views.chat, name="chat"),
    path("<str:room_name>/", views.room, name="room"),
]