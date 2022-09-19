from .base import *

DEBUG = False

ADMINS = (
    (env("USER"), env("EMAIL")),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": {
        
    }
}
