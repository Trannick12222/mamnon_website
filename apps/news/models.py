from django.db import models
from apps.core.models import TimeStampedModel

class News(TimeStampedModel):
    title = models.CharField(max_length=200, verbose_name="Tiêu đề")
    content = models.TextField(verbose_name="Nội dung")
    is_published = models.BooleanField(default=True, verbose_name="Đã xuất bản")
    
    class Meta:
        verbose_name = "Tin tức"
        verbose_name_plural = "Tin tức & Bài viết"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title