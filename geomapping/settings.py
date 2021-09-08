import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-v&%eu7)@=2so-nlts2w4$ll16gsf8(0ikecl=$wrx(5$holg6o'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_filters',
    'widget_tweaks',
    'crispy_forms',
    'django.contrib.gis',
    'leaflet',
    'mapping',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'geomapping.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'geomapping.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'abu_dhabi',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PASSWORD': 'admin',
        'PORT': '5432',
    }
}

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

SITE_ID = 1
LANGUAGE_CODE = 'en'
TIME_ZONE = 'Asia/Dubai'
USE_I18N = True
USE_L10N = True
USE_TZ = True



STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'geomapping/static'),
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LANGUAGES = [
    ('en', _('English')),
    ('ar', _('Arabic')),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (24.466667, 54.366669),
    'DEFAULT_ZOOM': 10,
    'MIN_ZOOM': 1,
    'MAX_ZOOM': 21,
    'SCALE': 'both',
    'ATTRIBUTION_PREFIX': 'Abu Dhabi Geo Mapping System',
    'TILES': [('Satellite', 'http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}', {'attribution': 'Developed by Azhar Saleem', 'maxZoom': 20, 'subdomains': ['mt0', 'mt1', 'mt2', 'mt3']})]
}