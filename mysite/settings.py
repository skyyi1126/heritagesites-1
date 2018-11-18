"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from mysite import secrets

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets.SECRET_KEY
# SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

# WARNING: test_without_migrations app must appear before any other apps
# in INSTALLED_APPS that provide a custom test management command.
# See https://pypi.org/project/django-test-without-migrations/

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local
    'api.apps.ApiConfig',
    'heritagesites.apps.HeritagesitesConfig',

    # Third-party
    'corsheaders',
    'crispy_forms',
    'django_filters',
    'rest_framework',
    'rest_framework_swagger',
    'social_django',
    'test_without_migrations',
]

# https://pypi.org/project/django-cors-headers/
# CorsMiddleware should be placed as high as possible, especially before any middleware that can
# generate responses such as Django’s CommonMiddleware or Whitenoise’s WhiteNoiseMiddleware.
# If it is not before, it will not be able to add the CORS headers to these responses.
# Also if you are using CORS_REPLACE_HTTPS_REFERER it should be placed before Django’s
# CsrfViewMiddleware."

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

# A list of origin hostnames that are authorized to make cross-site HTTP requests.
# The value 'null' can also appear in this list, and will match the Origin: null header
# that is used in “privacy-sensitive contexts”, such as when the client is running from
# a file:// domain. Defaults to [].
CORS_ORIGIN_WHITELIEST = (
    '127.0.0.1:3000/'
)

# Use Django's standard `django.contrib.auth` permissions, or allow read-only access for
# unauthenticated users.
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

ROOT_URLCONF = 'mysite.urls'

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

# django-crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Add a custom test runner for converting unmanaged models to managed before
# running a test and then revert the effect afterwards.
TEST_RUNNER = 'heritagesites.utils.UnManagedModelTestRunner'

# test_without_migration setting that ensures you don’t lose any additional
# functionality provided by your custom test management command.

# TEST_WITHOUT_MIGRATIONS_COMMAND = 'django_nose.management.commands.test.Command'

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'unesco_heritage_sites',
        'USER': 'django',
        'OPTIONS': {
            'read_default_file': '/etc/mysql/my.cnf',
        },
    }
}

# Authentication backends
# Must include the default Django Auth backend for the admin site
AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    # 'social_core.backends.google.GoogleOAuth',
    # 'social_core.backends.twitter.TwitterOAuth',
    # 'social_core.backends.yahoo.YahooOpenId',
    'django.contrib.auth.backends.ModelBackend',
)

# Social Auth namespace
SOCIAL_AUTH_URL_NAMESPACE = 'social'

# Oauth key and secret
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = secrets.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = secrets.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

# Login routes
LOGIN_URL = '/auth/login/google-oauth2/'
# LOGIN_URL = 'login'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'
# TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
# https://stackoverflow.com/questions/8687927/django-static-static-url-static-root
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static")