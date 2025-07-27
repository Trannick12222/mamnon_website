from django.db import models
from apps.core.models import TimeStampedModel

class Testimonial(TimeStampedModel):
    parent_name = models.CharField(max_length=100, verbose_name="Tên phụ huynh")
    content = models.TextField(verbose_name="Nội dung đánh giá")
    is_featured = models.BooleanField(default=False, verbose_name="Nổi bật")
    
    class Meta:
        verbose_name = "Đánh giá"
        verbose_name_plural = "Đánh giá phụ huynh"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Đánh giá của {self.parent_name}"