import uuid
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.utils.timezone import timezone

# Create your models here.
class Staff(models.Model):
    PRINCIPAL = "Principal"
    TEACHER = "Teacher"
    ASSISTANT = "Assistant"
    COUNSELOR = "Counselor"
    TITLES = {
      "PRINCIPAL": "Principal",
      "TEACHER": "Teacher",
      "ASSISTANT": "Assistant",
      "COUNSELOR": "Counselor",
    }
    MATH = "Math"
    ENGLISH = "English"
    ADMIN = "Admin"
    SCIENCE = "Science"
    NOTHING = "N/A"
    DEPARTMENTS = {
      "MATH": "Math",
      "ENGLISH": "English",
      "ADMIN": "Admin",
      "SCIENCE": "Science",
      "NOTHING": "N/A"
    }
    user = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE,
    )
    employee_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(
      max_length=30,
      choices=TITLES,
      default=TEACHER,
    )
    department = models.CharField(
      max_length=30,
      choices=DEPARTMENTS,
      default=NOTHING
    )
    phone_message = 'Phone number must be entered in the format: 05999999999'
    phone_regex = RegexValidator(
      regex=r'^(05)\d{9}$',
      message=phone_message
    )
    phone = models.CharField(validators=[phone_regex], max_length=60, null=True, blank=True)
    
      
class Parents(models.Model):
    FATHER = "Father"
    MOTHER = "Mother"
    GUARDIAN = "Guardian"
    RELATIONSHIPS = {
      "FATHER": "Father",
      "MOTHER": "Mother",
      "GUARDIAN": "Guardian",
    }
    id = models.UUIDField(primary_key=True, default=str(uuid), editable=False)
    user = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE,
    )
    relationship = models.CharField(
      max_length=30,
      choices=RELATIONSHIPS,
    )
    phone_message = 'Phone number must be entered in the format: 05999999999'
    phone_regex = RegexValidator(
      regex=r'^(05)\d{9}$',
      message=phone_message
    )
    phone = models.CharField(validators=[phone_regex], max_length=60, null=True, blank=True)
  
  
class Students(models.Model):
    user = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE,
    )
    student_id = models.UUIDField(primary_key=True, default=str(uuid.uuid4), editable=False)
    grade_level = models.IntegerField(choices=[(i, str(i)) for i in range(1, 13)])
    homeroom_teacher = models.ForeignKey(
      "Staff",
      on_delete=models.CASCADE,
    ) 
    parents = models.ManyToManyField(
      Parents,
    )
    date_of_birth = models.DateField()
    
    
class Announcements(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.title

class Events(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
      

    

'''
class StudentParent(models.Model):
    student_id = models.ForeignKey(
      "Students",
      on_delete=models.CASCADE,
    )
    id = models.ForeignKey(
      "Parents",
      on_delete=models.CASCADE,
    )
    '''