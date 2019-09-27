
import datetime
import os
from dotenv import load_dotenv, find_dotenv
from pathlib import *

load_dotenv(find_dotenv())
env_path = Path('.') / '.env'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG")

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'Fundooapi',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'rest_framework',
    'rest_framework_swagger',
    'storages',
    'Notes',
    # 'SocialLogin'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'FundooApp.urls'

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

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'FundooApp.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv("DATABASES_NAME"),
            'USER': os.getenv("DATABASES_USER"),
            'PASSWORD': os.getenv("DATABASES_PASSWORD"),
            'HOST': 'localhost',
            'PORT': '5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

EMAIL_USE_TLS = True
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':
        ('rest_framework.permissions.IsAuthenticatedOrReadOnly',),

}


JWT_AUTH = {

    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=12000),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',

}

SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'api_version': '0.1',
    'enabled_methods': [
        'get',
        'post'
    ],
    'SECURITY_DEFINATIONS': {
        "api_key": {
            "type": "apikey",
            "name": "Authorization",
            "in": "header"
        },
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# STATIC_URL = '/static/'

# AWS app settings.

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = 'ap-south-1'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'FundooApp/static'),
]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

# SOCIAL LOGIN
#  GitHub
SOCIAL_AUTH_GITHUB_KEY = os.getenv('SOCIAL_AUTH_GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = os.getenv('SOCIAL_AUTH_GITHUB_SECRET')
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'

# FaceBook
SOCIAL_AUTH_FACEBOOK_KEY = "2473108862809792"
SOCIAL_AUTH_FACEBOOK_SECRET = "561be24fd9ec3fb0a67f1bbfaaa619fb"

# AUTHENTICATION BACKEND

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    # 'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# REDIS_CREDENTIALS
REDIS_HOST = 'localhost'
REDIS_PORT = '6379'
REDIS_USERNAME = ""
REDIS_PASSWORD = ""


# MEDIA FILES
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
