from decouple import config

env = config('ENV', 'development')

if env == 'production':
    from .production import *
elif env == 'test':
    from .test import *
else:
    from .development import *
