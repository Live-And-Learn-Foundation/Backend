# Generated by Django 5.1.2 on 2024-10-14 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thesis',
            name='more_info',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
