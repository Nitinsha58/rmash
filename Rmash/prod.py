import json

with open('/etc/config.json') as config_file:
    config = json.load(config_file)


# If using in your own project, update the project namespace below
from Rmash.base import * 

SECRET_KEY = config['SECRET_KEY']

# False if not in os.environ
DEBUG = config['DEBUG']

ALLOWED_HOSTS = config['ALLOWED_HOSTS']
CSRF_TRUSTED_ORIGINS = config['CSRF_TRUSTED_ORIGINS']

#API KEYS
CLIENT_ID = env('CLIENT_ID')
CLIENT_SECRET = env('CLIENT_SECRET')
API_KEY = env('API_KEY')

# Database settings
DATABASES = {
    'default': {
        'ENGINE': config['db']['ENGINE'],
        'NAME': config['db']['NAME'],
        'USER': config['db']['USER'],
        'PASSWORD': config['db']['PASSWORD'],
        'HOST': config['db']['HOST'],
        'PORT': config['db']['PORT'],
    }
}