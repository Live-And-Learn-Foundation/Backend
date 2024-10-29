# Generated by Django 5.1.2 on 2024-10-27 05:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_userdetail_user_user_user_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_detail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='users.userdetail'),
        ),
    ]
