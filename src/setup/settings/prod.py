from .base import *

DEBUG = False

ADMINS = (
    (env("USER"), env("EMAIL")),
)

ALLOWED_HOSTS = ['django-elearning.com', 'www.django-elearning.com']

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': '5432',
    }
}

SECURE_SSL_REDIRECT = True # redireciona as requisições HTTP para HTTPs
CSRF_COOKIE_SECURE = True # cookie seguro
