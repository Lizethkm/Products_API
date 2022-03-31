# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#80yv6gj^rtkgl4h8)7u50m$_p@i$lo&wclipcb_+77)s!87d%'




# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Password'
    }
}