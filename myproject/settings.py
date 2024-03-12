"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iw+b1%p9&zw_+#gx+m&aw$gza2-_p6$03s3&4p+4kbd8%o0b_8'

# SECURITY WARNING: don't run with debug turned on in production!
if 'PYTHONPATH' in os.environ:
    Debug = True
    # Debug = False
    ALLOWED_HOSTS = ['.ap-northeast-1.elasticbeanstalk.com']
else:
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True
    ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'myproject',
    'tasks',
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

ROOT_URLCONF = 'myproject.urls'

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

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''
if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
            'default': {
                'ENGINE':'django.db.backends.postgresql_psycopg2',
                'NAME': os.environ['RDS_DB_NAME'],
                'USER': os.environ['RDS_USERNAME'],
                'PASSWORD': os.environ['RDS_PASSWORD'],
                'HOST': os.environ['RDS_HOSTNAME'],
                'PORT': os.environ['RDS_PORT'],
            }
        }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'todosdbdom',
            'USER': 'postgres',
            'PASSWORD': '2021Sh@des!',
            'HOST': 'localhost',
            'PORT':'5432',
        },
    }

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Pacific/Auckland'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# Resource - https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/
if 'S3_BUCKET' in os.environ:
    # aws settings
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    print("IS IT HERE??")
    print(AWS_ACCESS_KEY_ID)
 
    AWS_SECRET_ACCESS_KEY = os.environ['SECRET_KEY']
    print("IS IT HERE??")
    print(AWS_SECRET_ACCESS_KEY)
 
    AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET']
    print("IS IT HERE??")
    print(AWS_STORAGE_BUCKET_NAME)
 
    AWS_S3_REGION_NAME = 'ap-northeast-1'
 
    #AWS_DEFAULT_ACL = 'public-read'
    AWS_DEFAULT_ACL = None
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
 
    print("IS IT HERE??")
    print(AWS_S3_CUSTOM_DOMAIN)
 
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    # s3 static settings
    AWS_LOCATION = 'static'
 
    STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    print("IS IT HERE??")
    print(STATIC_URL)
 
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
else:   
    STATIC_URL = '/static/'
    # STATIC_ROOT = os.path.join(BASE_DIR, 'static')
 
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
 
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
