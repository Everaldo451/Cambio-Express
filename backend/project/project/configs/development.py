from .base import *

DEBUG = True

SECRET_KEY = secrets.token_urlsafe(50)
LOGGING["root"] = {
    "handlers": ["console"],
    "level": "DEBUG"
}
