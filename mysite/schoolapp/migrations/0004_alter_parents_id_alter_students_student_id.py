# Generated by Django 5.0.6 on 2024-08-15 09:07

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parents',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='students',
            name='student_id',
            field=models.UUIDField(default='<function uuid4 at 0xffff9dfbae80>', editable=False, primary_key=True, serialize=False),
        ),
    ]
