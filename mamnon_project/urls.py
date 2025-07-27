from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.core.views import contact_form, kindergarten_home

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # URL cho form liên hệ
    path('contact-form/', contact_form, name='contact_form'),
    
    # URL cho trang chủ custom (nếu cần)
    path('kindergarten/', kindergarten_home, name='kindergarten_home'),
    
    # URLs cho các apps khác
    path('contacts/', include('apps.contacts.urls')),
    path('news/', include('apps.news.urls')),
    path('programs/', include('apps.programs.urls')),
    
    # Django CMS URLs (phải để cuối cùng)
    path('', kindergarten_home, name='home'),
]

# Serve static files trong development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)