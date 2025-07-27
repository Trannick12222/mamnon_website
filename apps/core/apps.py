# apps/core/apps.py
from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'
    verbose_name = 'Thông tin cơ bản'

# ==========================================
# apps/schools/apps.py
from django.apps import AppConfig

class SchoolsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.schools'
    verbose_name = 'Quản lý lớp học'

# ==========================================
# apps/programs/apps.py  
from django.apps import AppConfig

class ProgramsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.programs'
    verbose_name = 'Chương trình học'

# ==========================================
# apps/news/apps.py
from django.apps import AppConfig

class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.news'
    verbose_name = 'Tin tức & Bài viết'

# ==========================================
# apps/testimonials/apps.py
from django.apps import AppConfig

class TestimonialsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.testimonials' 
    verbose_name = 'Đánh giá phụ huynh'

# ==========================================
# apps/contacts/apps.py
from django.apps import AppConfig

class ContactsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.contacts'
    verbose_name = 'Liên hệ & Đăng ký'