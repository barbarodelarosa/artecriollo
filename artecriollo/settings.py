"""
Django settings for artecriollo project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
from pathlib import Path
import environ
import os


env = environ.Env()

environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = env('DEBUG')
DEBUG = False
# TEMPLATE_DEBUG = DEBUG

# ALLOWED_HOSTS = ['artecriollo.nat.cu','www.artecriollo.nat.cu','152.206.118.246']
ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites', 
]
#MY APPS
INSTALLED_APPS += [
    'core',
    'shop',
    'auction',
    # 'authy',
    'profile',
    'newsletters',
    'blog',
    'affiliate',
    'notifications',
    'lottery',
    'utils',
]
# OTHER APPS
INSTALLED_APPS += [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
  
    'djcelery_email',
    'crispy_forms',
    'ckeditor',

    'django_crontab',
    'captcha',
    'mapbox_location_field',

  
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # 'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'artecriollo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'artecriollo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': env('NAME_DB'),
        'USER': env('USER_DB'),
        'PASSWORD': env('PASSWORD_DB'),
        'HOST': env('HOST_DB'),
        'PORT': env('PORT_DB'),
    }
}


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


AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]



# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Havana'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "static_root")
STATIC_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")



# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CRISPY_TEMPLATE_PACK = 'bootstrap4'


# if DEBUG is False:

#     SESSION_COOKIE_SECURE = True
#     SECURE_BROWSER_XSS_FILTER = True
#     SECURE_CONTENT_TYPE_NOSNIFF = True
#     SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#     SECURE_HSTS_SECONDS = 31536000
#     SECURE_REDIRECT_EXEMPT = []
#     SECURE_SSL_REDIRECT = True
#     SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https') 

#     # EMAIL_BACKEND = 'django.core.mail.smtp.EmailBackend'

#     ALLOWED_HOSTS = ["https://artecriollo.nat.cu", "https://artecriollo.pythonanywhere.com"]

#     DATABASES = {
#         'default':{
#             'ENGINE': 'django.db.backends.mysql',
#              'NAME': '',
#              'USER': '',
#              'PASSWORD': '',
#              'HOST': '',
#              'PORT': '',
#          }
#     }


#ENZONA
KEY_ACCESS_TOKEN=env('KEY_ACCESS_TOKEN')
CONSUMER_USER=env('CONSUMER_USER')
CONSUMER_PASSWORD=env('CONSUMER_PASSWORD')
URL_API_ENZONA=env('URL_API_ENZONA')





SITE_ID = 1
ACCOUNT_AUTHENTICATON_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ACCOUNT_EMAIL_VERIFICATION = 'optional'
# LOGIN_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = "/profile/"

import os
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
        messages.DEBUG: 'secondary',
        messages.INFO: 'info',
        messages.SUCCESS: 'success',
        messages.WARNING: 'warning',
        messages.ERROR: 'danger',
 }


#*********************************************
#EMAIL CONFIG

EMAIL_FROM = env('EMAIL_FROM')
EMAIL_BCC = env('EMAIL_BCC')

EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
# EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#************************************************************


# DEFAULT_FROM_EMAIL= env('DEFAULT_FROM_EMAIL')
# EMAIL_HOST_USER='mail@mail.com'


DEFAULT_FROM_EMAIL=env('DEFAULT_FROM_EMAIL')
NOTIFY_EMAIL= env('NOTIFY_EMAIL')
EMAIL_FROM=env('EMAIL_FROM')
EMAIL_BCC=env('EMAIL_BCC')
EMAIL_HOST=env('EMAIL_HOST')
EMAIL_PORT=587
EMAIL_HOST_USER=env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=env('EMAIL_HOST_PASSWORD')
# EMAIL_USE_SSL=False
EMAIL_USE_TLS=True # SI SE DESHABILITA DA PROBLEMA EN EL SERVIDOR
# EMAIL_USE_SSL=False


CRONJOBS = [
    ('*/1 * * * *', 'lottery.cron.my_scheduled_job'),
    ('*/1 * * * *', 'auction.cron.my_scheduled_job'),
    ('*/1 * * * *', 'core.cron.my_scheduled_job_save_db'),
]

RECAPTCHA_PUBLIC_KEY = '6Lcp5zQgAAAAABxMCgINkEovuLi0EACYhB3cVZZV'
RECAPTCHA_PRIVATE_KEY = '6Lcp5zQgAAAAALew8jCJfdKzX3lpdenqCyfnGX2O'

ACCOUNT_SIGNUP_FORM_CLASS = 'core.forms.AllAuthSignupForm'
RECAPTCHA_REQUIRED_SCORE = 0.50


ACCOUNT_FORMS = {
    'login': 'core.forms.MyCustomLoginForm',
    # 'signup': 'allauth.account.forms.SignupForm',
    # 'add_email': 'allauth.account.forms.AddEmailForm',
    # 'change_password': 'allauth.account.forms.ChangePasswordForm',
    # 'set_password': 'allauth.account.forms.SetPasswordForm',
    # 'reset_password': 'allauth.account.forms.ResetPasswordForm',
    # 'reset_password_from_key': 'allauth.account.forms.ResetPasswordKeyForm',
    # 'disconnect': 'allauth.socialaccount.forms.DisconnectForm',
}
GOOGLE_RECAPTCHA_SECRET_KEY='6Lcp5zQgAAAAALew8jCJfdKzX3lpdenqCyfnGX2O'




MAPBOX_KEY ="pk.eyJ1IjoiYXJ0ZWNyaW9sbG8iLCJhIjoiY2wzd2gyZHZyMDI1ZjNjbXkzNmduNmdydiJ9.eJ7_JqzaIEHZ4rGFBA0Ung"
