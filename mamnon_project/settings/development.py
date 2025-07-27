from .base import *

# Debug mode
DEBUG = True

# Allowed hosts cho development
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# Email backend cho development (in console)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# TẮT Debug Toolbar tạm thời
# if DEBUG:
#     INSTALLED_APPS += ['debug_toolbar']
#     MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE

# Cache cho development (dummy cache)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Django CMS settings cho development
CMS_TOOLBAR_ANONYMOUS_ON = True