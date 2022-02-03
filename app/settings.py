import os
from telnetlib import AUTHENTICATION
# import environ 

# env = environ.Env()

# environ.Env.read_env()

SECRET_KEY = 'k652upe&97+)a1c++mn%9$!6pdir=)0f27qkhwb#vxo(7&)-0&'

DEBUG = True


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    'crispy_forms',
    'core',
    'cart',
]

DEFAULT_FROM_EMAIL = 'mail@gmail.com'
NOTIFY_EMAIL = 'mail@gmail.com'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
     
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

STATIC_ROOT = os.path.join(BASE_DIR, "static_root")

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

PAYPAL_CLIENT_ID = 'AdewaqkxlrEBULgMx4F8wK3g6EY4Km3xIWpxsrHv5BbVBCrxiplEpo38YkIY7xjB8W4RdEJx4DYSiJwW'

PAYPAL_SECRET_KEY = 'EIy-886_AhB5rGOXhjNVgqie-3MgWgXNp8_BiEc2gErt-01SLoeRZE7qmVW7VjTguLIQQXKT-Vv6-raC'


if DEBUG is False:
    
    SESSION_COOKIE_SECURE = True
    SESSION_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HOST_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_REDIRECT_EXEMPT = []
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    
    ALLOWED_HOSTS = ['https://harvalley.com']
    
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    
    DATABASES = {
        
        'default': {
            
            'ENGIINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'harvalley',
            'USER': '',
            'PASSWORD': '',	
            'HOST': '',
            'PORT': '',
            
        }
        
    }
    
    PAYPAL_CLIENT_ID = 'live'

    PAYPAL_SECRET_KEY = 'live'