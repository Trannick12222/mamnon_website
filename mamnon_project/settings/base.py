import os
from pathlib import Path
from decouple import config

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='django-insecure-change-this-key')

# Application definition
DJANGO_APPS = [
    'djangocms_admin_style',  # CMS admin style (phải đặt trước django.contrib.admin)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

CMS_APPS = [
    'cms',
    'menus',
    'treebeard',
    'sekizai',
    'djangocms_text_ckeditor',
]

THIRD_PARTY_APPS = [
    'easy_thumbnails',
    'image_cropping',  # PHẢI sau easy_thumbnails
    'filer',
    # 'compressor',  # Uncomment for production optimization
]

# Fixed: Remove duplicate apps
LOCAL_APPS = [
    'apps.core',
    'apps.schools',
    'apps.programs', 
    'apps.news',
    'apps.testimonials',
    'apps.contacts',
]

INSTALLED_APPS = DJANGO_APPS + CMS_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Middleware
MIDDLEWARE = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

ROOT_URLCONF = 'mamnon_project.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
            # Support for component-based templates
            BASE_DIR / 'templates' / 'components',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
                'apps.core.context_processors.hero_settings',  # Legacy - giữ hero_bg
                'apps.core.context_processors.site_data',      # Mới - data cho design mới
                'apps.core.context_processors.school_info',    # Legacy - thông tin trường
            ],
        },
    },
]

WSGI_APPLICATION = 'mamnon_project.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
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

# Internationalization
LANGUAGE_CODE = 'vi'
TIME_ZONE = 'Asia/Ho_Chi_Minh'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Languages
LANGUAGES = [
    ('vi', 'Tiếng Việt'),
    ('en', 'English'),
]

# Static files (CSS, JavaScript, Images) - Optimized for Tailwind
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Static files optimization
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'compressor.finders.CompressorFinder',  # Uncomment for production
]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Site ID (required for Django CMS)
SITE_ID = 1

# Django CMS Settings
CMS_TEMPLATES = [
    ('cms/home.html', 'Trang chủ'),
    ('cms/page.html', 'Trang nội dung'),
    ('cms/contact.html', 'Liên hệ'),
    ('base.html', 'Base Template với Tailwind'),  # Added for Tailwind
]

# CMS Permissions
CMS_PERMISSION = True

# CMS Language settings
CMS_LANGUAGES = {
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'vi',
            'hide_untranslated': False,
            'name': 'Tiếng Việt',
            'redirect_on_fallback': True,
        },
    ],
}

# CMS Toolbar
CMS_TOOLBAR_ANONYMOUS_ON = False

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Hoặc SMTP server của bạn
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='your-email@gmail.com')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='your-app-password')
DEFAULT_FROM_EMAIL = 'Sunny Kids <your-email@gmail.com>'

# Security settings
X_FRAME_OPTIONS = 'SAMEORIGIN'
SECURE_FRAME_DENY = False

# Django CMS specific settings
CMS_TOOLBAR_URL__EDIT_ON = 'edit'
CMS_TOOLBAR_URL__EDIT_OFF = 'edit_off'
CMS_TOOLBAR_URL__BUILD = 'build'
CMS_WIZARD_ENABLE = False
CMS_CONFIRM_VERSION4 = True

# ==================== IMAGE PROCESSING & THUMBNAILS ====================

# Easy Thumbnails configuration
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'easy_thumbnails.processors.scale_and_crop',
    'easy_thumbnails.processors.filters',
)

# Optimized thumbnail aliases for responsive design
THUMBNAIL_ALIASES = {
    '': {
        # Hero slides với responsive breakpoints
        'hero_xl': {'size': (1920, 1080), 'crop': True, 'quality': 95},      # Desktop large
        'hero_lg': {'size': (1534, 862), 'crop': True, 'quality': 90},       # Desktop
        'hero_md': {'size': (1200, 675), 'crop': True, 'quality': 85},       # Tablet landscape
        'hero_sm': {'size': (800, 450), 'crop': True, 'quality': 80},        # Tablet portrait
        'hero_xs': {'size': (640, 360), 'crop': True, 'quality': 75},        # Mobile
        
        # Program cards (4:3 ratio)
        'program_lg': {'size': (400, 300), 'crop': True, 'quality': 85},
        'program_md': {'size': (300, 225), 'crop': True, 'quality': 80},
        'program_sm': {'size': (200, 150), 'crop': True, 'quality': 75},
        
        # Staff photos (1:1 square)
        'staff_lg': {'size': (400, 400), 'crop': True, 'quality': 90},
        'staff_md': {'size': (200, 200), 'crop': True, 'quality': 85},
        'staff_sm': {'size': (120, 120), 'crop': True, 'quality': 80},
        
        # Gallery images (flexible)
        'gallery_lg': {'size': (800, 600), 'crop': True, 'quality': 90},
        'gallery_md': {'size': (600, 400), 'crop': True, 'quality': 85},
        'gallery_sm': {'size': (300, 200), 'crop': True, 'quality': 80},
        'gallery_thumb': {'size': (150, 150), 'crop': True, 'quality': 75},
        
        # News thumbnails (16:10 ratio)
        'news_lg': {'size': (800, 500), 'crop': True, 'quality': 90},
        'news_md': {'size': (400, 250), 'crop': True, 'quality': 85},
        'news_sm': {'size': (320, 200), 'crop': True, 'quality': 80},
        
        # Admin previews
        'admin_preview': {'size': (150, 100), 'crop': True, 'quality': 80},
    }
}

# Image cropping settings
IMAGE_CROPPING_JQUERY_URL = None  # Sử dụng jQuery có sẵn
IMAGE_CROPPING_SIZE_WARNING = True
IMAGE_CROPPING_BACKEND = 'image_cropping.backends.easy_thumbs.EasyThumbnailsBackend'

# ==================== TAILWIND CSS SETTINGS ====================

# Tailwind CSS development settings
TAILWIND_CSS_DEV_MODE = config('DEBUG', default=True, cast=bool)

# Content Security Policy for Tailwind (development)
if TAILWIND_CSS_DEV_MODE:
    # Allow inline styles for Tailwind CDN in development
    CSP_STYLE_SRC = ["'self'", "'unsafe-inline'", "https://cdn.tailwindcss.com", "https://fonts.googleapis.com"]
    CSP_SCRIPT_SRC = ["'self'", "'unsafe-inline'", "https://cdn.tailwindcss.com"]
    CSP_FONT_SRC = ["'self'", "https://fonts.gstatic.com"]
else:
    # Strict CSP for production
    CSP_STYLE_SRC = ["'self'", "https://fonts.googleapis.com"]
    CSP_SCRIPT_SRC = ["'self'"]
    CSP_FONT_SRC = ["'self'", "https://fonts.gstatic.com"]

# ==================== PERFORMANCE OPTIMIZATION ====================

# Caching (for production)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'TIMEOUT': 300,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}

# Session optimization
SESSION_CACHE_ALIAS = 'default'
SESSION_COOKIE_AGE = 1209600  # 2 weeks

# ==================== LOGGING ====================

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'django.log',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'root': {
        'handlers': ['console'],
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'apps': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'tailwind': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

# Tạo thư mục logs nếu chưa có
LOGS_DIR = BASE_DIR / 'logs'
LOGS_DIR.mkdir(exist_ok=True)

# ==================== CUSTOM SETTINGS ====================

# Custom context data for templates
SITE_CONTEXT = {
    'site_name': 'Sunny Kids',
    'site_description': 'Mầm non song ngữ quốc tế hàng đầu tại TP.HCM',
    'default_image': '/static/images/logo.png',
    'social_media': {
        'facebook': 'https://facebook.com/sunnykids',
        'youtube': 'https://youtube.com/sunnykids',
        'instagram': 'https://instagram.com/sunnykids',
    }
}

# Contact form settings
CONTACT_EMAIL = config('CONTACT_EMAIL', default='info@sunnykids.edu.vn')
ADMIN_EMAIL = config('ADMIN_EMAIL', default='admin@sunnykids.edu.vn')

# File upload settings
FILE_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024  # 5MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024  # 10MB

# ==================== INTERNATIONALIZATION ====================

# Locale paths
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# Date and number formats
DATE_FORMAT = 'd/m/Y'
DATETIME_FORMAT = 'd/m/Y H:i'
SHORT_DATE_FORMAT = 'd/m/y'