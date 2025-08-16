from decouple import config
from .base import *

DEBUG = False

SECRET_KEY = config("SECRET_KEY")
ALLOWED_HOSTS = ['localhost', '0.0.0.0']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT')
    }
}

