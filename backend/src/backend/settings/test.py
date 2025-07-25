import secrets
from .base import *

DEBUG = True

SECRET_KEY = secrets.token_urlsafe(50)
LOGGING["root"] = {
    "handlers": ["console"],
    "level": "DEBUG"
}
LOGGING["handlers"]["request"] = {
    "class": "logging.StreamHandler"
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}
