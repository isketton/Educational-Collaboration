import uuid
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):

  USER_ROLES = (
    ("staff", "Staff"), 
    ("parent", "Parent"),
    ("student", "Student"),
  )
  role = models.CharField(max_length=10, blank=False, choices=USER_ROLES) 
  email = models.EmailField(unique=True)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  date_joined = models.DateField(default=timezone.now)
    
  def __str__(self):
    return "{}".format(self.get_full_name())

class Address(models.Model):
    city = models.CharField("City", max_length=80)
    state = models.CharField("State", max_length=80)
    zip_code = models.CharField(max_length=12)
    country = models.CharField("Country", max_length=30)
    address = models.CharField("Address", max_length=128)

class Schools(models.Model):
    GRADE_LEVELS = {
      "E": "Elementary",
      "M": "Middle",
      "H": "High"
    }
    name = models.CharField(max_length=30)
    address = models.ForeignKey(
      Address,
      on_delete=models.CASCADE,
      null=True
    )
    grade_level = models.CharField(max_length=1, choices=GRADE_LEVELS, default="N/A")
    # will send in school info to be reviewed. Will approve by admin, if not admin will delete
    # this flag is just to signify it has not been looked at yet
    certified = models.BooleanField(default=False)
    
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
    school_id = models.ForeignKey(
      Schools,
      on_delete=models.CASCADE,
      default=1,
    )
    user_id = models.OneToOneField(
      CustomUser,
      on_delete=models.CASCADE,
      related_name="staff_account"
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
    
    def __str__(self):
        return self.title
      
class Parents(models.Model):
    id = models.UUIDField(primary_key=True, default=str(uuid), editable=False)
    user_id = models.OneToOneField(
      CustomUser,
      on_delete=models.CASCADE,
      related_name="parent_account"
    )
    address = models.ForeignKey(
      Address,
      on_delete=models.CASCADE,
      null=True
    )
    phone_message = 'Phone number must be entered in the format: 05999999999'
    phone_regex = RegexValidator(
      regex=r'^(05)\d{9}$',
      message=phone_message
    )
    phone = models.CharField(validators=[phone_regex], max_length=60, null=True, blank=True)
  
  
class Students(models.Model):
    school_id = models.ForeignKey(
      "Schools",
      on_delete=models.CASCADE,
      default=1,
    )
    user_id = models.OneToOneField(
      CustomUser,
      on_delete=models.CASCADE,
      related_name="student_account"
    )
    parent = models.ForeignKey(
      Parents,
      on_delete=models.CASCADE,
      related_name="child",
      null=True
    )
    student_id = models.UUIDField(primary_key=True, default=str(uuid.uuid4), editable=False)
    grade_level = models.IntegerField(choices=[(i, str(i)) for i in range(1, 13)])
    homeroom_teacher = models.ForeignKey(
      Staff,
      on_delete=models.CASCADE,
    ) 
    address = models.ForeignKey(
      Address,
      on_delete=models.CASCADE,
      null=True
    )
    date_of_birth = models.DateField(auto_now_add=True)
    
    
class Announcements(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Events(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
      
class Report(models.Model):
    student_id = models.ForeignKey(
      Students,
      on_delete=models.CASCADE,
    )
    teacher_id = models.ForeignKey(
      Staff,
      on_delete=models.CASCADE,
    )
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    F = "F"
    GRADE = {
      "A": "A",
      "B": "B",
      "C": "C",
      "D": "D",
      "F": "F",
    }
    course = models.CharField(max_length=30)
    grades = models.CharField(max_length=1, choices=GRADE)
    comment = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    
class Assignments(models.Model):
    student_id = models.ForeignKey(
      Students,
      on_delete=models.CASCADE,
    )
    teacher_id = models.ForeignKey(
      Staff,
      on_delete=models.CASCADE,
    )
  
    title = models.CharField(max_length=30)
    score = models.DecimalField(max_digits=5, decimal_places=2) 
    
    def __str__(self):
        return self.title
      
class Clubs(models.Model):
    teacher_id = models.ManyToManyField(
      Staff,
    )
    students_id = models.ManyToManyField(
      Students,
    )
    name = models.CharField(max_length=30)
    content = models.TextField()
