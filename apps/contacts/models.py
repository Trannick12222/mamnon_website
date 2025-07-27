from django.db import models
from django.utils import timezone

class Contact(models.Model):
    """
    Model để lưu thông tin đăng ký tham quan
    """
    parent_name = models.CharField(max_length=100, verbose_name="Họ tên phụ huynh")
    phone = models.CharField(max_length=20, verbose_name="Số điện thoại")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    child_age = models.PositiveIntegerField(blank=True, null=True, verbose_name="Tuổi của bé")
    message = models.TextField(blank=True, null=True, verbose_name="Ghi chú")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Ngày tạo")
    is_contacted = models.BooleanField(default=False, verbose_name="Đã liên hệ")
    
    class Meta:
        verbose_name = "Liên hệ"
        verbose_name_plural = "Danh sách liên hệ"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.parent_name} - {self.phone}"

class Newsletter(models.Model):
    """
    Model cho đăng ký nhận tin tức
    """
    email = models.EmailField(unique=True, verbose_name="Email")
    subscribed_at = models.DateTimeField(default=timezone.now, verbose_name="Ngày đăng ký")
    is_active = models.BooleanField(default=True, verbose_name="Kích hoạt")
    
    class Meta:
        verbose_name = "Đăng ký newsletter"
        verbose_name_plural = "Danh sách newsletter"
        ordering = ['-subscribed_at']
    
    def __str__(self):
        return self.email