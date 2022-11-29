import os
from pathlib import Path
#import dj_database_url

#from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
#load_dotenv(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = 'change me'
if SECRET_KEY in os.environ:
    SECRET_KEY = os.environ["SECRET_KEY"]

PGPASSWORD = 'change me'
if PGPASSWORD in os.environ:
    PGPASSWORD = os.environ["PGPASSWORD"]
    print('password is ', PGPASSWORD)

DEBUG = True
ALLOWED_HOSTS = ['*'] # ['127.0.0.1', '.pythonanywhere.com']
# add .amazonaws.com to the ALLOWED_HOSTS if cloud9 is used
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
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
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

#DATABASE_URL = os.getenv("DATABASE_URL")
#DATABASE_URL = os.environ.get("DATABASE_URL")
#DATABASE_URL = 'postgresql://${{ PGUSER }}:${{ PGPASSWORD }}@${{ PGHOST }}:${{ PGPORT }}/${{ PGDATABASE }}'
'''
#windows
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blog-posts',
        'USER': 'postgres',
        'PASSWORD': 'pas1234!@#$',
        'HOST': 'localhost',
        'PORT': '5432',        
    }
}

DATABASES = {
    "default":  dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
 }
'''
#railway
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway', # os.environ["PGDATABASE"],
        'USER': 'postgres', # os.environ["PGUSER"],
        'PASSWORD': 'AwTzHbmwRyMsn61fiNWb', # os.environ["PGPASSWORD"],
        'HOST': 'containers-us-west-121.railway.app', # os.environ["PGHOST"],
        'PORT': '6165' # os.environ["PGPORT"],
    }
}

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC' # 'UTC-08:00'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MEDIA_URL =  '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
mimetypes.add_type("text/css", ".css", True)
'''