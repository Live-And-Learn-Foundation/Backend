# Generated by Django 5.1.2 on 2024-10-22 07:21

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='user_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='studentcourse',
            name='course_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
