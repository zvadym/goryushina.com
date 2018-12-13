"""
Django settings for testPr project.

Generated by 'django-admin startproject' using Django 1.11.16.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#-t(xar+g6r^!c%p44)r2_=_rm2v8uzd8(obzqh0$88hk7s%4q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'polymorphic',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Installed apps
    'gunicorn',
    'tinymce',
    'sorl.thumbnail',
    'stored_settings',

    # Project apps
    'apps.changelist_ordering',
    'apps.ui',
    'apps.page',
    'apps.gallery',
    'apps.menu',
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

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_files')

FILEBROWSER_DIRECTORY = 'mce_filebrowser/'

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'plugins': "embed,advimage,youtubeIframe,table,spellchecker,paste,searchreplace,inlinepopups",
    'width': 700,
    'height': 800,
    'theme_advanced_buttons1': "embed,youtubeIframe,image,|,pastetext,|,link,unlink,|,bold,italic,underline,strikethrough,address,|,justifyleft,justifycenter,justifyright,justifyfull,|,formatselect,|,table,removeformat,code",
    'theme_advanced_buttons2': "",
    'theme_advanced_buttons3': "",
    'theme_advanced_buttons4': "",
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_statusbar_location': "bottom",
    'theme_advanced_resizing': True,
    'theme_advanced_resizing_min_width': 700,
    'theme_advanced_resizing_max_width': 700,
    'theme_advanced_resizing_min_height': 700,
    'theme_advanced_resizing_max_height': 1200,

    'relative_urls': False,
    'verify_html': False,
    'valid_elements': '*[*]',
}

try:
    from .local import *
except ImportError:
    pass
