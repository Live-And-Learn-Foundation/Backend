from . import BASE_DIR
from ..scopes import scopes, default_scopes
from oauth.tokens import signed_token_generator
import os
from os.path import join
from dotenv import load_dotenv

CONFIG_ENV_PATH = join(BASE_DIR, 'config.env')
load_dotenv(CONFIG_ENV_PATH)

# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
APP_NAME = os.getenv("APP_NAME", "Course")

SECRET_KEY = os.getenv("SECRET_KEY")

JWKS_URL = os.getenv("JWKS_URL", "http://127.0.0.1:8000/api/auth/v1/oauth/jwks/")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "True") == "True"

API_HOST = os.getenv("API_HOST")

DEFAULT_HOST = os.getenv("DEFAULT_HOST", "localhost:8001")

ALLOWED_HOSTS = os.getenv(
    'DJANGO_ALLOWED_HOSTS',
    default=f"{DEFAULT_HOST.split(':')[0]},host.docker.internal"
).split(',')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    "rest_framework_api_key",
    'corsheaders',
    'django_filters',
    'health_check',
    'base',
    'courses',
]

MIDDLEWARE = [
    'django.middlewares.security.SecurityMiddleware',
    'django.contrib.sessions.middlewares.SessionMiddleware',
    'django.middlewares.common.CommonMiddleware',
    'django.contrib.auth.middlewares.AuthenticationMiddleware',
    'django.contrib.messages.middlewares.MessageMiddleware',
    'django.middlewares.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middlewares.CorsMiddleware',
    'base.middlewares.exception_handling.ExceptionHandlingMiddleware',
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

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",  # To keep the Browsable API
)

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["oauth.permissions.TokenHasActionScope"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "oauth.authentication.CustomJWTAuthentication",
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

# Static config
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
