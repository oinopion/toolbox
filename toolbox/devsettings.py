from defaultsettings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Hack around IDEA
OLD_INSTALLED_APPS = INSTALLED_APPS

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'toolbox.workload',
    'toolbox.people',
    'toolbox.stories',
]

INSTALLED_APPS = list(OLD_INSTALLED_APPS)
INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)

# debug_toolbar settings
MIDDLEWARE_CLASSES.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
INTERNAL_IPS = ['127.0.0.1']
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}
