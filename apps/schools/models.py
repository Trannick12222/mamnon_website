from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.core.models import TimeStampedModel

class AgeGroup(TimeStampedModel):
    """Nhóm tuổi"""
    name = models.CharField(max_length=100, verbose_name="Tên nhóm tuổi")
    min_age_months = models.IntegerField(
        verbose_name="Tuổi tối thiểu (tháng)",
        validators=[MinValueValidator(12), MaxValueValidator(84)]
    )
    max_age_months = models.IntegerField(
        verbose_name="Tuổi tối đa (tháng)", 
        validators=[MinValueValidator(12), MaxValueValidator(84)]
    )
    description = models.TextField(blank=True, verbose_name="Mô tả")
    
    class Meta:
        verbose_name = "Nhóm tuổi"
        verbose_name_plural = "Nhóm tuổi"
        ordering = ['min_age_months']
    
    def __str__(self):
        return f"{self.name} ({self.min_age_months}-{self.max_age_months} tháng)"

class Teacher(TimeStampedModel):
    """Giáo viên"""
    name = models.CharField(max_length=100, verbose_name="Họ tên")
    email = models.EmailField(blank=True, verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Số điện thoại")
    
    # Thông tin chuyên môn
    position = models.CharField(
        max_length=100,
        verbose_name="Chức vụ"
    )
    specialization = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Chuyên môn"
    )
    experience_years = models.IntegerField(
        verbose_name="Năm kinh nghiệm",
        validators=[MinValueValidator(0)]
    )
    education = models.TextField(verbose_name="Trình độ học vấn")
    bio = models.TextField(verbose_name="Tiểu sử")
    
    is_active = models.BooleanField(default=True, verbose_name="Đang làm việc")
    is_featured = models.BooleanField(default=False, verbose_name="Giáo viên nổi bật")
    
    class Meta:
        verbose_name = "Giáo viên"
        verbose_name_plural = "Đội ngũ giáo viên"
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} - {self.position}"

class ClassType(TimeStampedModel):
    """Loại lớp học"""
    name = models.CharField(max_length=100, verbose_name="Tên loại lớp")
    age_group = models.ForeignKey(
        AgeGroup, 
        on_delete=models.CASCADE,
        verbose_name="Nhóm tuổi"
    )
    max_students = models.IntegerField(
        verbose_name="Sĩ số tối đa",
        validators=[MinValueValidator(5), MaxValueValidator(25)]
    )
    teacher_ratio = models.CharField(
        max_length=10,
        verbose_name="Tỷ lệ giáo viên/trẻ",
        help_text="Ví dụ: 1:3"
    )
    
    # Thông tin chương trình
    program_type = models.CharField(
        max_length=20,
        choices=[
            ('bilingual', 'Song ngữ'),
            ('english', 'Tiếng Anh'),
            ('vietnamese', 'Tiếng Việt'),
        ],
        default='bilingual',
        verbose_name="Loại chương trình"
    )
    
    # Học phí
    monthly_fee = models.DecimalField(
        max_digits=10, 
        decimal_places=0,
        verbose_name="Học phí hàng tháng (VND)"
    )
    
    description = models.TextField(verbose_name="Mô tả chương trình")
    is_active = models.BooleanField(default=True, verbose_name="Đang tuyển sinh")
    
    class Meta:
        verbose_name = "Loại lớp học"
        verbose_name_plural = "Loại lớp học"
        ordering = ['age_group__min_age_months', 'name']
    
    def __str__(self):
        return f"{self.name} - {self.age_group.name}"