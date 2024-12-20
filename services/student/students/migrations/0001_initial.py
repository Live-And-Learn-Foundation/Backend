# Generated by Django 5.1.2 on 2024-10-13 09:28

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id',
                 models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('enrollment_year', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'students',
            },
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id',
                 models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('enrollment_date', models.DateField(blank=True, null=True)),
                ('student',
                 models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='students',
                                   to='students.student')),
            ],
            options={
                'db_table': 'student_courses',
            },
        ),
    ]
