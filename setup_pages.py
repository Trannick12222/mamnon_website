import os
import django

# Cấu hình môi trường Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mamnon_project.settings.development')
django.setup()

from cms.api import create_page
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site

# Lấy admin user (tạo nếu chưa tồn tại)
User = get_user_model()
admin, created = User.objects.get_or_create(username="admin", defaults={"is_staff": True, "is_superuser": True})
if created:
    admin.set_password("admin123")
    admin.save()
    print("✅ Tạo user admin với password: admin123")

# Lấy site mặc định
site, _ = Site.objects.get_or_create(id=1, defaults={"domain": "localhost:8000", "name": "Localhost"})

# Tạo page Trang chủ
page = create_page(
    title="Trang chủ",
    template="cms/home.html",
    language="vi",
    created_by=admin.username,
    in_navigation=True,
    site=site  # 👈 Gán site trực tiếp
)

# Publish page
from cms.api import publish_page
publish_page(page, user=admin, language="vi")
print("✅ Tạo và publish Trang chủ thành công.")
