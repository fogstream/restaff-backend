import os
from restaff.settings.base import *

SECRET_KEY = os.getenv('SECRET_KEY', 'sdfsdf')

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_DB', 'restaff'),
        'USER': os.getenv('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'restaff'),
        'HOST': os.getenv('POSTGRES_HOST', '0.0.0.0'),
        'PORT': os.getenv('POSTGRES_PORT', '5436'),
    }
}


