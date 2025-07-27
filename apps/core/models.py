from django.db import models
from django.urls import reverse
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from django.db import models
from image_cropping import ImageCropField, ImageRatioField

class HeroSetting(models.Model):
    background = ImageCropField(
        "Ảnh nền Hero",
        upload_to="hero_backgrounds/",
        null=True,
        blank=True,
    )
    cropping = ImageRatioField('background', '1534x512')
    
    def __str__(self):
        return "Hero background setting"
class TimeStampedModel(models.Model):
    """Abstract base class với timestamp"""
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")
    
    class Meta:
        abstract = True

class SEOModel(models.Model):
    """Abstract base class cho SEO"""
    meta_title = models.CharField(
        max_length=60, 
        blank=True, 
        verbose_name="Tiêu đề SEO",
        help_text="Tối đa 60 ký tự"
    )
    meta_description = models.TextField(
        max_length=160, 
        blank=True, 
        verbose_name="Mô tả SEO",
        help_text="Tối đa 160 ký tự"
    )
    meta_keywords = models.CharField(
        max_length=255, 
        blank=True, 
        verbose_name="Từ khóa SEO",
        help_text="Các từ khóa cách nhau bằng dấu phẩy"
    )
    
    class Meta:
        abstract = True

class SchoolInfo(TimeStampedModel):
    """Thông tin cơ bản về trường"""
    name = models.CharField(max_length=200, verbose_name="Tên trường")
    slogan = models.CharField(max_length=300, blank=True, verbose_name="Slogan")
    description = models.TextField(verbose_name="Mô tả về trường")
    
    # Thông tin liên hệ
    address = models.TextField(verbose_name="Địa chỉ")
    phone = models.CharField(max_length=20, verbose_name="Số điện thoại")
    email = models.EmailField(verbose_name="Email")
    website = models.URLField(blank=True, verbose_name="Website")
    
    # Giờ hoạt động
    working_hours = models.CharField(
        max_length=100, 
        default="7:00 - 18:00",
        verbose_name="Giờ hoạt động"
    )
    working_days = models.CharField(
        max_length=100,
        default="Thứ 2 - Thứ 6", 
        verbose_name="Ngày hoạt động"
    )
    
    # Hình ảnh
    logo = FilerImageField(
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL,
        related_name="school_logos",  # ← THÊM related_name
        verbose_name="Logo trường"
    )
    hero_image = FilerImageField(
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL,
        related_name="school_hero_images",  # ← THÊM related_name
        verbose_name="Hình ảnh chính"
    )
    
    # Social media
    facebook_url = models.URLField(blank=True, verbose_name="Facebook")
    youtube_url = models.URLField(blank=True, verbose_name="YouTube") 
    instagram_url = models.URLField(blank=True, verbose_name="Instagram")
    
    # Tài liệu
    brochure = FilerFileField(
        null=True,
        blank=True, 
        on_delete=models.SET_NULL,
        related_name="school_brochures",  # ← THÊM related_name
        verbose_name="Brochure (PDF)"
    )
    
    class Meta:
        verbose_name = "Thông tin trường"
        verbose_name_plural = "Thông tin trường"
    
    def __str__(self):
        return self.name

class Gallery(TimeStampedModel):
    """Thư viện ảnh"""
    title = models.CharField(max_length=200, verbose_name="Tiêu đề")
    description = models.TextField(blank=True, verbose_name="Mô tả")
    image = FilerImageField(
        on_delete=models.CASCADE,
        related_name="gallery_images",  # ← THÊM related_name
        verbose_name="Hình ảnh"
    )
    category = models.CharField(
        max_length=50,
        choices=[
            ('classroom', 'Lớp học'),
            ('playground', 'Sân chơi'),
            ('activities', 'Hoạt động'),
            ('events', 'Sự kiện'),
            ('meals', 'Bữa ăn'),
        ],
        default='activities',
        verbose_name="Danh mục"
    )
    is_featured = models.BooleanField(default=False, verbose_name="Nổi bật")
    order = models.IntegerField(default=0, verbose_name="Thứ tự")
    
    class Meta:
        verbose_name = "Hình ảnh"
        verbose_name_plural = "Thư viện ảnh"
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return self.title

class FAQ(TimeStampedModel):
    """Câu hỏi thường gặp"""
    question = models.CharField(max_length=500, verbose_name="Câu hỏi")
    answer = models.TextField(verbose_name="Câu trả lời")
    category = models.CharField(
        max_length=50,
        choices=[
            ('admission', 'Tuyển sinh'),
            ('tuition', 'Học phí'),
            ('curriculum', 'Chương trình học'),
            ('facilities', 'Cơ sở vật chất'),
            ('health', 'Sức khỏe'),
            ('other', 'Khác'),
        ],
        default='other',
        verbose_name="Danh mục"
    )
    is_active = models.BooleanField(default=True, verbose_name="Hiển thị")
    order = models.IntegerField(default=0, verbose_name="Thứ tự")
    
    class Meta:
        verbose_name = "Câu hỏi thường gặp"
        verbose_name_plural = "Câu hỏi thường gặp"
        ordering = ['order', 'question']
    
    def __str__(self):
        return self.question

class Achievement(TimeStampedModel):
    """Thành tích, giải thưởng"""
    title = models.CharField(max_length=200, verbose_name="Tên giải thưởng")
    description = models.TextField(blank=True, verbose_name="Mô tả")
    year = models.IntegerField(verbose_name="Năm")
    image = FilerImageField(
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="achievement_images",  # ← THÊM related_name
        verbose_name="Hình ảnh"
    )
    is_featured = models.BooleanField(default=False, verbose_name="Nổi bật")
    
    class Meta:
        verbose_name = "Thành tích"
        verbose_name_plural = "Thành tích & Giải thưởng"
        ordering = ['-year', 'title']
    
    def __str__(self):
        return f"{self.title} ({self.year})"