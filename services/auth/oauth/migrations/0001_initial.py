# Generated by Django 5.1.1 on 2024-10-12 12:33

import oauth2_provider.generators
import oauth2_provider.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('token_checksum', oauth2_provider.models.TokenChecksumField(db_index=True, max_length=64, unique=True)),
                ('expires', models.DateTimeField()),
                ('scope', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('token', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ApiKey',
            fields=[
                ('id', models.CharField(editable=False, max_length=150, primary_key=True, serialize=False, unique=True)),
                ('prefix', models.CharField(editable=False, max_length=8, unique=True)),
                ('hashed_key', models.CharField(editable=False, max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('name', models.CharField(default=None, help_text='A free-form name for the API key. Need not be unique. 50 characters max.', max_length=50)),
                ('revoked', models.BooleanField(blank=True, default=False, help_text='If the API key is revoked, clients cannot use it anymore. (This cannot be undone.)')),
                ('expiry_date', models.DateTimeField(blank=True, help_text='Once API key expires, clients cannot use it anymore.', null=True, verbose_name='Expires')),
                ('scope', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'API key',
                'verbose_name_plural': 'API keys',
                'ordering': ('-created',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('client_id', models.CharField(db_index=True, default=oauth2_provider.generators.generate_client_id, max_length=100, unique=True)),
                ('redirect_uris', models.TextField(blank=True, help_text='Allowed URIs list, space separated')),
                ('post_logout_redirect_uris', models.TextField(blank=True, default='', help_text='Allowed Post Logout URIs list, space separated')),
                ('client_type', models.CharField(choices=[('confidential', 'Confidential'), ('public', 'Public')], max_length=32)),
                ('authorization_grant_type', models.CharField(choices=[('authorization-code', 'Authorization code'), ('implicit', 'Implicit'), ('password', 'Resource owner password-based'), ('client-credentials', 'Client credentials'), ('openid-hybrid', 'OpenID connect hybrid')], max_length=32)),
                ('client_secret', oauth2_provider.models.ClientSecretField(blank=True, db_index=True, default=oauth2_provider.generators.generate_client_secret, help_text='Hashed on Save. Copy it now if this is a new secret.', max_length=255)),
                ('hash_client_secret', models.BooleanField(default=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('skip_authorization', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('algorithm', models.CharField(blank=True, choices=[('', 'No OIDC support'), ('RS256', 'RSA with SHA-2 256'), ('HS256', 'HMAC with SHA-2 256')], default='', max_length=5)),
                ('allowed_origins', models.TextField(blank=True, default='', help_text='Allowed origins list to enable CORS, space separated')),
                ('scope', models.TextField(blank=True)),
                ('type', models.CharField(blank=True, choices=[('system', 'The applications created by Pandosima Company'), ('third-party', "The third-parties's applications"), ('client', 'The application created by the bussiness')], default='client', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=255, unique=True)),
                ('expires', models.DateTimeField()),
                ('redirect_uri', models.TextField()),
                ('scope', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('code_challenge', models.CharField(blank=True, default='', max_length=128)),
                ('code_challenge_method', models.CharField(blank=True, choices=[('plain', 'plain'), ('S256', 'S256')], default='', max_length=10)),
                ('nonce', models.CharField(blank=True, default='', max_length=255)),
                ('claims', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IDToken',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('jti', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='JWT Token ID')),
                ('expires', models.DateTimeField()),
                ('scope', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RefreshToken',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=255)),
                ('token_family', models.UUIDField(blank=True, editable=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('revoked', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]