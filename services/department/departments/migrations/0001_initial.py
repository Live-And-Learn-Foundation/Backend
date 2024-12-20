# Generated by Django 5.1.2 on 2024-10-14 15:43

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
            name='Department',
            fields=[
                ('id',
                 models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('more_info', models.JSONField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'departments',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id',
                 models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
            options={
                'db_table': 'teachers',
            },
        ),
        migrations.CreateModel(
            name='TeacherType',
            fields=[
                ('id',
                 models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'teacher_types',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id',
                 models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('more_info', models.JSONField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('department', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE,
                                                 related_name='departments_major', to='departments.department')),
            ],
            options={
                'db_table': 'majors',
            },
        ),
        migrations.CreateModel(
            name='TeacherCourse',
            fields=[
                ('id',
                 models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('teacher', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE,
                                              related_name='teachers_teacher_course', to='departments.teacher')),
            ],
            options={
                'db_table': 'teacher_courses',
            },
        ),
        migrations.CreateModel(
            name='TeacherDepartment',
            fields=[
                ('id',
                 models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE,
                                                 related_name='departments_teacher_department',
                                                 to='departments.department')),
                ('teacher',
                 models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='teachers',
                                   to='departments.teacher')),
            ],
            options={
                'db_table': 'teacher_departments',
            },
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher_type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='teacher_types', to='departments.teachertype'),
        ),
    ]
