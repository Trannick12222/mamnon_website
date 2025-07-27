from django.db import models
from apps.core.models import TimeStampedModel

class Program(TimeStampedModel):
    name = models.CharField(max_length=200, verbose_name="Tên chương trình")
    description = models.TextField(verbose_name="Mô tả")
    is_active = models.BooleanField(default=True, verbose_name="Hoạt động")
    
    class Meta:
        verbose_name = "Chương trình"
        verbose_name_plural = "Chương trình học"
    
    def __str__(self):
        return self.name