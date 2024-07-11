'''import os
from django.db import migrations
from dotenv import load_dotenv

load_dotenv()



class Migration(migrations.Migration):
    dependencies = []
    
    def generate_superuser(apps, schema_editor):  
      from django.contrib.auth.models import User
      
      DJANGO_DB_NAME = os.environ.get('DJANGO_DB_NAME', "defualt")
      DJANGO_SU_NAME = os.environ.get('DJANGO_SU_NAME')
      DJANGO_SU_EMAIL = os.environ.get('DJANGO_SU_EMAIL')
      DJANGO_SU_PASSWORD = os.environ.get('DJANGO_SU_PASSWORD')
      
      superuser = User.objects.create_superuser(
        username=DJANGO_SU_NAME,
        email=DJANGO_SU_EMAIL,
        password=DJANGO_SU_PASSWORD
      )
      superuser.save()
    
      operations = [
        migrations.RunPython(generate_superuser),
      ]'''
      
      
import logging
import environ
from django.db import migrations

logger = logging.getLogger(__name__)

def generate_superuser(apps, schema_editor):
    from django.contrib.auth import get_user_model

    env = environ.Env()
    USERNAME = env.str("DJANGO_SU_NAME")
    PASSWORD = env.str("DJANGO_SU_PASSWORD")
    EMAIL = env.str("DJANGO_SU_EMAIL")

    user = get_user_model()

    if not user.objects.filter(username=USERNAME, email=EMAIL).exists():
        logger.info("Creating new superuser")
        admin = user.objects.create_superuser(
           username=USERNAME, password=PASSWORD, email=EMAIL
        )
        admin.save()
    else:
        logger.info("Superuser already created!")


class Migration(migrations.Migration):
   dependencies = []

   operations = [migrations.RunPython(generate_superuser)]