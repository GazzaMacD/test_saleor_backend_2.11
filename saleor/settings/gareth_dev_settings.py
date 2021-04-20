
from django.core.exceptions import ImproperlyConfigured

from .base_settings import *


# set django settings module environ variable with the following
# export DJANGO_SETTINGS_MODULE=saleor.settings.my_dev_settings 
  

#Allowed Hosts
ALLOWED_CLIENT_HOSTS = get_sec("ALLOWED_CLIENT_HOSTS")
ALLOWED_CLIENT_HOSTS = get_list(ALLOWED_CLIENT_HOSTS)

INTERNAL_IPS = get_list(os.environ.get("INTERNAL_IPS", "127.0.0.1"))

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_sec('DEV_DB_NAME'),
        'USER': get_sec('DEV_DB_USER'),
        'PASSWORD': get_sec('DEV_DB_PW'),
        'HOST': get_sec('DEV_DB_HOST'),
        'PORT': '',
        'CONN_MAX_AGE': 600,
        'TEST': {
            'NAME': get_sec('DEV_TEST_DB'),
        },
    }
}

