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
]

CUSTOM_APPS = [ 
    'apps.contacts',
    'apps.core',
    'apps.news',
    'apps.programs',
    'apps.schools',
    'apps.testimonials',
    ]

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
        'DIRS': [BASE_DIR / 'templates'],
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

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
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
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
DEFAULT_FROM_EMAIL = 'Sunny Kids <your-email@gmail.com>'

# Thêm vào cuối file base.py
X_FRAME_OPTIONS = 'SAMEORIGIN'

# Hoặc nếu vẫn lỗi, dùng:
# X_FRAME_OPTIONS = 'ALLOWALL'

# Django CMS specific settings
CMS_TOOLBAR_ANONYMOUS_ON = True
CMS_TOOLBAR_URL__EDIT_ON = 'edit'
CMS_TOOLBAR_URL__EDIT_OFF = 'edit_off'
CMS_TOOLBAR_URL__BUILD = 'build'

# Security settings cho development
SECURE_FRAME_DENY = False
CMS_WIZARD_ENABLE = False
CMS_CONFIRM_VERSION4 = True
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'easy_thumbnails.processors.scale_and_crop',
    'easy_thumbnails.processors.filters',
)

# Cấu hình thumbnail aliases
THUMBNAIL_ALIASES = {
    '': {
        'hero': {'size': (1534, 512), 'crop': True, 'quality': 95},
    },
}

# Cho phép crop tự do (không bắt buộc tỉ lệ cố định)
IMAGE_CROPPING_JQUERY_URL = None  # Sử dụng jQuery có sẵn
IMAGE_CROPPING_SIZE_WARNING = True