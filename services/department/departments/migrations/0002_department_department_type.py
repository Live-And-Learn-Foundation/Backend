# Generated by Django 5.1.2 on 2024-10-18 14:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='department_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
