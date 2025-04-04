# Generated by Django 5.0.6 on 2024-08-15 22:41

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0004_alter_parents_id_alter_students_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='student_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
