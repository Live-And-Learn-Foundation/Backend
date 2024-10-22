# Generated by Django 5.1.2 on 2024-10-20 19:25

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('degree', models.CharField(blank=True, max_length=100, null=True)),
                ('academic_title', models.CharField(blank=True, max_length=100, null=True)),
                ('biography', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'users_detail',
            },
        ),
    ]