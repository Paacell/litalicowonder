"""
Django settings for progress_management project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url

import os
from pathlib import Path
from dotenv import load_dotenv

# 環境変数を読み込む
load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k+e*uzzlyjyy8#s)kxt%wil)*!pocgk7h61ko7-dek_6ysy!-c'

DEBUG = os.getenv('DEBUG', 'False') == 'True'

if DEBUG:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']
else:
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'ex_course_data.onrender.com').split(',')

import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default=os.getenv("DATABASE_URL"))
}

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ex_course_data',
        'USER': 'ex_course_data_user',
        'PASSWORD': 'tg8Tx9txMzg7iyrdEDxzEwHsWouUvsW5',
        'HOST': 'dpg-cus33o56l47c73afklgg-a',
        'PORT': '5432',
        'OPTIONS': {
            'application_name': 'accounts'
        }
    }
}


CSRF_TRUSTED_ORIGINS = [
    "https://ex_course_database.onrender.com",
]


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

ALLOWED_HOSTS = ["progress_management.onrender.com", "localhost", "127.0.0.1"]


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'dashboard',
    'progress',
    'portfolio',
    'goals',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'progress_management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'progress_management.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.CustomUser'



# Renderでの静的ファイル配信設定
if os.getenv("RENDER"):
    import dj_database_url
    DATABASES["default"] = dj_database_url.config()
    MIDDLEWARE += ["whitenoise.middleware.WhiteNoiseMiddleware"]
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
