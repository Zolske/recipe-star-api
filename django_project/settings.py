"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 3.2.15.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
import re

# if the file env.py exist (only in local production), than import env
if os.path.exists('env.py'):
    import env

CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}

# let Django know where to find media files, like images
MEDIA_URL = '/media/'

# set the default file storage to Cloudinary
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# for Jason web token
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d %b %Y',
}
if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]

REST_USE_JWT = True
JWT_AUTH_SECURE = True
# access token
JWT_AUTH_COOKIE = 'my-app-auth'
# refresh token
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
# Allow front end app and api be deployed to different platforms
JWT_AUTH_SAMESITE = 'None'

# over write the default serializer
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'django_project.serializers.CurrentUserSerializer'
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# from original source // "recipe-star" app
#ALLOWED_HOSTS = [
#    'recipe-star-api.herokuapp.com',
#    'localhost',
#]
                                                                                   
# UPDATE 'recipe-star-api.herokuapp.com'
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOST'), 'localhost']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'rest_framework',
    'django_filters',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'corsheaders',

    # app
    'profiles',
    'recipes',
    'comments',
    'likes',
    'followers'
]

SITE_ID = 1

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        # 'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': ({
        # development
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        # production
    } if 'DEV' in os.environ else dj_database_url.parse(
        os.environ.get('DATABASE_URL')
    ))
}


# Allow Cookies
CORS_ALLOW_CREDENTIALS = True

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# tells django where to find the static files
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# MEDIA_URL = '/media/'
# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


#### switch between the 2 for local and deployed version, rebuild on heroku ########## 
                                                                                     #
#### use for deployed app ############################################################               
# ORIGINAL Set the ALLOWED_ORIGINS for the network requests made to the server #######
#if 'CLIENT_ORIGIN' in os.environ:                                                   #
#    CORS_ALLOWED_ORIGINS = [                                                        #
#        os.environ.get('CLIENT_ORIGIN')                                             #
#    ]                                                                               #
#else:                                                                               #
#    CORS_ALLOWED_ORIGIN_REGEXES = [                                                 #
#        r"^https://.*\.gitpod\.io$",                                                #
#    ]                                                                               #
                                                                                     #
# use for deployed version                                                           #
DEBUG = 'DEV' in os.environ                                                          #
                                                                                     #
####  use for local app ##############################################################
if 'CLIENT_ORIGIN_DEV' in os.environ:                                                #
    extracted_url = re.match(                                                        #
        r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)    #
    CORS_ALLOWED_ORIGIN_REGEXES = [                                                  #
        rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",                                #
    ]                                                                                #
                                                                                     #
# don't run with debug turned on in production, but use to access amin panel with css#
#DEBUG = True                                                                        #
######################################################################################