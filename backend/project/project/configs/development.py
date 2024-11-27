from .base import *

DEBUG = True

SECRET_KEY = secrets.token_urlsafe(50)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'test.sqlite3',
    }
}
