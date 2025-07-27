from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from apps.core.views import contact_form, kindergarten_home

# URLs không cần ngôn ngữ
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact-form/', contact_form, name='contact_form'),
]

# URLs có ngôn ngữ (cho CMS)
urlpatterns += i18n_patterns(
    # Custom URLs
    path('kindergarten/', kindergarten_home, name='kindergarten_home'),
    path('contacts/', include('apps.contacts.urls')),
    path('news/', include('apps.news.urls')),
    path('programs/', include('apps.programs.urls')),
    
    # Django CMS URLs (PHẢI có để CMS hoạt động)
    path('', include('cms.urls')),
)

# Serve static files trong development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)