#configuraciones del proyecto que son necesarias para ejecutarlas de forma local
#aca van las configuraciones de fase de desarrollo

from .base import * #esto me importa del archivo base toda la configuracion para el DATABASE


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!w&$=0c9qt1088mz6m8h1acwga_al@)u!28n_vp^!!=2@_je9a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*'] 


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
