from decouple import config
from .base import *
import os

DEBUG = False

#Secret Key
SECRET_KEY = config("SECRET_KEY")

#CORS
ALLOWED_HOSTS = ['localhost', '0.0.0.0']

#Static Files
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'staticfiles')

#Database
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

