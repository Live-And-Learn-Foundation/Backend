from . import BASE_DIR
from ..scopes import scopes, default_scopes
from oauth.tokens import signed_token_generator
import os
from os.path import join, dirname
from dotenv import load_dotenv


CONFIG_ENV_PATH = join(BASE_DIR, 'config.env')
load_dotenv(CONFIG_ENV_PATH)


# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

OIDC_RSA_PRIVATE_KEY_FILE = os.getenv("OIDC_RSA_PRIVATE_KEY_FILE")

if OIDC_RSA_PRIVATE_KEY_FILE:
    OIDC_RSA_PRIVATE_KEY_FILE = (
        join(BASE_DIR, OIDC_RSA_PRIVATE_KEY_FILE)
        if not OIDC_RSA_PRIVATE_KEY_FILE.startswith("/")
        else OIDC_RSA_PRIVATE_KEY_FILE
    )
    with open(OIDC_RSA_PRIVATE_KEY_FILE) as f:
        OIDC_RSA_PRIVATE_KEY = f.read()
else:
    raise ValueError(
        "OIDC_RSA_PRIVATE_KEY_FILE environment variable is not set.")

JWT_ISSUER = os.getenv("JWT_ISSUER", "Docs")

DEBUG = os.getenv("DEBUG", "True") == "True"
API_HOST = os.getenv("API_HOST")

DEFAULT_HOST = os.getenv("DEFAULT_HOST", "localhost:8000")

ALLOWED_HOSTS = os.getenv(
    "DJANGO_ALLOWED_HOSTS", "127.0.0.1:8000,localhost,host.docker.internal").split(',')
DEFAULT_CLIENT_SECRET = os.getenv("DEFAULT_CLIENT_SECRET")
DEFAULT_CLIENT_ID = os.getenv("DEFAULT_CLIENT_ID")
SUPER_ADMIN_EMAIL = os.getenv("SUPER_ADMIN_EMAIL", "service@email.com")
SUPER_ADMIN_PASSWORD = os.getenv("SUPER_ADMIN_PASSWORD", "")

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = os.getenv(
    "DEFAULT_FROM_EMAIL", "Docs <noreply@email.com>")

DEFAULT_OAUTH2_SCHEME = "http" if API_HOST in [
    "localhost", "127.0.0.1"] else "https"
API_PORT = "8000"
DEFAULT_OAUTH2_PORT = ":" + API_PORT if API_PORT is not None else ""
OAUTH2_URL = DEFAULT_OAUTH2_SCHEME + "://" + API_HOST + DEFAULT_OAUTH2_PORT

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "rest_framework_api_key",
    'oauth2_provider',
    'corsheaders',
    'health_check',
    "base",
    'users',
    'oauth',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'base.middleware.exception_handling.ExceptionHandlingMiddleware',
    'base.middleware.decode_token.DecodeTokenMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            join(BASE_DIR, "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.mysql",
        'NAME': os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
        "OPTIONS": {"charset": "utf8mb4"},
    }
}

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = "users.User"

OAUTH2_PROVIDER = {
    "OIDC_ENABLED": True,
    "OIDC_RSA_PRIVATE_KEY": OIDC_RSA_PRIVATE_KEY,
    "SCOPES": scopes,
    "DEFAULT_SCOPES": default_scopes,
    "SCOPES_BACKEND_CLASS": "oauth.settings_scopes.SettingsScopes",
    "OAUTH2_VALIDATOR_CLASS": "oauth.oauth_validators.CustomOAuth2Validator",
    "ACCESS_TOKEN_GENERATOR": signed_token_generator(
        OIDC_RSA_PRIVATE_KEY, issuer=JWT_ISSUER
    ),
    "REFRESH_TOKEN_GENERATOR": "oauthlib.oauth2.rfc6749.tokens.random_token_generator",
    "ACCESS_TOKEN_EXPIRE_SECONDS": 3600,
    "REFRESH_TOKEN_GRACE_PERIOD_SECONDS": 4000,
}

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["oauth.permissions.TokenHasActionScope"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "base.pagination.CustomPagination",
    "PAGE_SIZE": 12,
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Ho_Chi_Minh'
USE_I18N = True
USE_TZ = True

CORS_ORIGIN_ALLOW_ALL = True

MEDIA_ROOT = join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# static config
STATIC_URL = 'static/'
