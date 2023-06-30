"""
Django settings for MVPlayer project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import cloudinary_storage
import dotenv # <- New

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Add .env variables anywhere before SECRET_KEY
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# UPDATE secret key


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&v#7hg25wnqjuo0#5dtx3=y70g=o!t^p&ute753)lqg30(itt-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Music.apps.MusicConfig',
    'Video.apps.VideoConfig',
    'authentication.apps.AuthenticationConfig',
    # external
    'crispy_forms',
    'widget_tweaks',
    'cloudinary_storage',
    'cloudinary',
    #allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.facebook',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MVPlayer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    },
]

WSGI_APPLICATION = 'MVPlayer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    
    'default' : {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    # 'ENGINE' : 'django.db.backends.mysql',
    # 'NAME' : os.environ['DB_NAME'],
    # 'USER' : os.environ['DB_USER'],
    # 'PASSWORD' : os.environ['DB_PASSWORD'],
    # 'HOST' : 'localhost',
    # 'PORT' : '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ['CLOUD_NAME'],
    'API_KEY': os.environ['API_KEY'],
    'API_SECRET': os.environ['API_SECRET']
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# CSRF_TRUSTED_ORIGINS = [
#     'http://localhost:8000',
#     # 'https://sangeet.up.railway.app/'
# ],
# ALLOWED_HOSTS = [
#     'localhost',
#     # 'https://sangeet.up.railway.app'
# ],
# CORS_ORIGIN_WHITELIST = [
#     'http://localhost:8000',
#     # 'https://sangeet.up.railway.app'
# ]
CORS_ORIGIN_WHITELIST = [    'https://sangeet.up.railway.app',]

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR/'static']
STATIC_ROOT = BASE_DIR/'staticfiles'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')
MEDIA_URL = 'media/'

import mimetypes
mimetypes.add_type("text/css", ".css", True)
MEDIA_ROOT = BASE_DIR/'media'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.RawMediaCloudinaryStorage'
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



CRISPY_TEMPLATE_PACK = 'bootstrap4'

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)


SITE_ID = 1

ACCOUNT_EMAIL_VERIFICATION = 'none'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'index'
# LOGOUT_REDIRECT_URL = 'index'

SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'offline',
        }
    }
}
CRISPY_TEMPLATE_PACK = os.environ['CRISPY_TEMPLATE_PACK']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']