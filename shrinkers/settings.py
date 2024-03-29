"""
Django settings for shrinkers project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from google.oauth2 import service_account
import json


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# settings for MEDIA FILE
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


print(MEDIA_ROOT)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY_A = json.load(open(os.path.join(BASE_DIR, "keys.json"))).get("SECRET_KEY_A")
SECRET_KEY = SECRET_KEY_A

# SECURITY WARNING: don't run with debug turned on in production!
ENV = os.environ.get("DJANGO_ENV", "dev")

if ENV == "dev":
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.sites",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "shortener.apps.ShortenerConfig",
    "django_user_agents",
    "rest_framework",
    "drf_yasg",
    # allauth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # provider
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.github",
]


SITE_ID = 1

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        "APP": {"client_id": "123", "secret": "456", "key": ""}
    }
}


REST_FRAMEWORK = {
    # "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    # "PAGE_SIZE": 20,
}


INTERNAL_IPS = [
    "127.0.0.1",
]

LOGIN_URL = "/login"

ACCOUNT_SESSION_REMEMBER = True
SESSION_COOKIE_AGE = 3600

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_user_agents.middleware.UserAgentMiddleware",
    "shortener.middleware.ShrinkersMiddleware",
]

# if DEBUG:
#     MIDDLEWARE += [
#         'debug_toolbar.middleware.DebugToolbarMiddleware',
#     ]

GEOIP_PATH = os.path.join(BASE_DIR, "geolite2")
GEOIP_COUNTRY = os.path.join(BASE_DIR, "geolite2/GeoLite2-Country.mmdb")

ROOT_URLCONF = "shrinkers.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "shrinkers.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
db_password = json.load(open(os.path.join(BASE_DIR, "keys.json"))).get("DB_PASSWORD")
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "app_db",
        "USER": "root",
        "PASSWORD": db_password,
        "HOST": "34.64.254.216",
        "PORT": 3306,
        "OPTIONS": {"autocommit": True, "charset": "utf8mb4"},
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# try:
#     EMAIL_ID = json.load(open(os.path.join(BASE_DIR, "keys.json"))).get("email")
#     EMAIL_PW = json.load(open(os.path.join(BASE_DIR, "keys.json"))).get("email_pw")
# except Exception:
#     EMAIL_ID = None
#     EMAIL_PW = None
STATIC_URL = "static/"
# if DEBUG:
#     STATIC_URL = "static/"
# else:
#     # SECRET_KEY = json.load(open(os.path.join(BASE_DIR, "keys.json"))).get("service_key")
#     # GS_CREDENTIALS = service_account.Credentials.from_service_account_info(SECRET_KEY)
#     GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
#         os.path.join(BASE_DIR, "shrinkers/service_key.json")
#     )
#     STORAGES = {
#         "default": {"BACKEND": "config.storage_backends.GoogleCloudMediaStorage"},
#         "staticfiles": {"BACKEND": "config.storage_backends.GoogleCloudStaticStorage"},
#     }
#     GS_BUCKET_NAME = "shrinkers-sonzwon"
#     STATIC_URL = f"https://storage.googleapis.com/{GS_BUCKET_NAME}/statics/"
#     # Default primary key field type
#     # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
