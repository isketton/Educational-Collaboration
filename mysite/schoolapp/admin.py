from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class CustomUserAdmin(UserAdmin):
  add_fieldsets = (
    (
        None,
        {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2",     
                       "first_name","last_name", "email", 
                       "is_active", "is_staff", "is_superuser", 
                       "groups", "user_permissions",),
        },
    ),
)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Address)
admin.site.register(Schools)
admin.site.register(Staff)
admin.site.register(Parents)
admin.site.register(Students)
admin.site.register(Announcements)
admin.site.register(Events)
admin.site.register(Report)
admin.site.register(Assignments)
admin.site.register(Clubs)