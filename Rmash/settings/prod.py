import environ
import os
import dj_database_url

# If using in your own project, update the project namespace below
from Rmash.settings.base import * 

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
env.read_env(os.path.join(BASE_DIR, '.env'))

# False if not in os.environ
DEBUG = env('DEBUG')

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS')

# Parse database connection url strings like psql://user:pass@127.0.0.1:8458/db
DATABASE_URL = os.environ("DATABASE_URL")
DATABASES = {
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
} 