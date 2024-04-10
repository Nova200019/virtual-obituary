import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '6+_(6czw@+gbm$5q@j6u#ubk^)19o&0+3wi!2u(%x^^y^!d(j#'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'stay-for-ever.azurewebsites.net', 'stay-for-ever.net']

INSTALLED_APPS = [

    # channels
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "whitenoise.runserver_nostatic",
    
    # My_apps.
    'blog',
    'users.apps.UsersConfig',
    'footer',
    'chat',

    # Third_party_apps.
    'crispy_forms',
    # taggit
    'taggit',
    #forthumbnails
    'imagekit', 
    'storages',

]

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location':  os.path.join(BASE_DIR, 'backup')}

ASGI_APPLICATION = 'blog_project.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'blog_project.urls'

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

WSGI_APPLICATION = 'blog_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'deadman',
        'USER': 'pdmpubcemp',
        'PASSWORD': '1920London',
        'HOST': 'deadman.mysql.database.azure.com',
        'PORT': '3306',

        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'MARS_Connection': 'True',
        },
    },
}


STATICFILES_STORAGE = ('whitenoise.storage.CompressedManifestStaticFilesStorage')

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


LANGUAGE_CODE = 'en-us'

USE_I18N = True

USE_L10N = True

USE_TZ = True




STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
AZURE_ACCOUNT_NAME = 'csb100320016ae5e2db'
AZURE_ACCOUNT_KEY = 'y/F96Xonj8qdOp019d2kTgwNU5Dube9mPprx1l3R3P4UdEb9DIcut946FEwdyALWluLREjEx22+ij+AStYinwtA=='
AZURE_CONTAINER = 'media'
MEDIA_URL = f'https://csb100320016ae5e2db.blob.core.windows.net/media'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'blog:home'
LOGIN_URL = 'login'

ADMIN_SITE_HEADER = "BUDDIES"

TIME_ZONE =  'Asia/Kolkata'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
