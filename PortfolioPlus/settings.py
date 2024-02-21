from pathlib import Path
import configparser
import djongo

BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG = configparser.RawConfigParser()
CONFIG.read(BASE_DIR / 'config.ini')

SECRET_KEY = CONFIG['DEFAULT']['DjangoKey']
DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "befrimon.oxfff.ru",
    "oxfff.ru",
    "bfn-dev.ru"
]

INSTALLED_APPS = [
    "handbook.apps.HandbookConfig",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django_hosts',
]

MIDDLEWARE = [
    #'django_hosts.middleware.HostsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'PortfolioPlus.urls'
ROOT_HOSTCONF = 'PortfolioPlus.hosts'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'PortfolioPlus.jinja2.environment'
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'PortfolioPlus.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'devumid',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': CONFIG['DATABASE']['host'],
            'port': int(CONFIG['DATABASE']['port']),
            'username': CONFIG['DATABASE']['uname'],
            'password': CONFIG['DATABASE']['passwd'],
            'authSource': CONFIG['DATABASE']['dbname'],
            'authMechanism': 'SCRAM-SHA-1'
        },
        'LOGGING': {
            'version': 1,
            'loggers': {
                'djongo': {
                    'level': 'DEBUG',
                    'propagate': False,
                }
            },
         },
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

#AUTH_PASSWORD_VALIDATORS = [
#    {
#        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#    },
#]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


STATIC_URL = 'static/'
STATIC_ROOT = ''
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

