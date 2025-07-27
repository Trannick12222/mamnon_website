from django.db import models
from django.urls import reverse
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from django.db import models
from image_cropping import ImageCropField, ImageRatioField

class TimeStampedModel(models.Model):
    """Abstract base class với timestamp"""
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")
    
    class Meta:
        abstract = True
class HeroSlide(TimeStampedModel):
    """Hero Slider với custom crop functionality"""
    title = models.CharField(max_length=200, verbose_name="Tiêu đề")
    subtitle = models.TextField(max_length=500, verbose_name="Mô tả")
    
    # ===== REGULAR IMAGE FIELD + CROP COORDINATES =====
    background = models.ImageField(
        "Ảnh nền",
        upload_to="hero_slides/",
        help_text="Tỉ lệ khuyến nghị: 1920x1080. Có thể crop sau khi upload."
    )
    
    # Store crop coordinates as text field
    cropping = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Crop coordinates",
        help_text="Format: x,y,width,height"
    )
    
    # Buttons
    primary_button_text = models.CharField(
        max_length=50, 
        default="Đăng ký tham quan",
        verbose_name="Text nút chính"
    )
    primary_button_link = models.CharField(
        max_length=200,
        default="#contact", 
        verbose_name="Link nút chính"
    )
    
    secondary_button_text = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Text nút phụ"
    )
    secondary_button_link = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Link nút phụ"
    )
    
    # Thứ tự và hiển thị
    order = models.IntegerField(default=0, verbose_name="Thứ tự")
    is_active = models.BooleanField(default=True, verbose_name="Hiển thị")
    
    class Meta:
        verbose_name = "Hero Slide"
        verbose_name_plural = "Hero Slides"
        ordering = ['order']
    
    def __str__(self):
        return f"{self.title} (Order: {self.order})"
    
    def get_cropped_image_url(self):
        """Trả về URL ảnh đã crop"""
        if not self.background:
            return None
            
        if not self.cropping:
            return self.background.url
            
        try:
            from easy_thumbnails.files import get_thumbnailer
            coords = self.cropping.split(',')
            if len(coords) == 4:
                x = int(round(float(coords[0])))
                y = int(round(float(coords[1])))
                w = int(round(float(coords[2])))
                h = int(round(float(coords[3])))
                box = (x, y, x + w, y + h)
                
                thumbnailer = get_thumbnailer(self.background)
                cropped_image = thumbnailer.get_thumbnail({
                    'size': (1534, 512),
                    'crop': 'smart',
                    'quality': 95,
                    'box': box,
                })
                return cropped_image.url
            else:
                return self.background.url
        except Exception as e:
            print(f"Error creating cropped thumbnail: {e}")
            return self.background.url
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

# ==================== HERO SLIDER ====================
class HeroSlide(TimeStampedModel):
    """Hero Slider với crop functionality - Quản lý tại: Thông tin cơ bản → Hero Slides"""
    title = models.CharField(max_length=200, verbose_name="Tiêu đề")
    subtitle = models.TextField(max_length=500, verbose_name="Mô tả")
    
    # ===== CROP FUNCTIONALITY (từ HeroSetting) =====
    background = ImageCropField(
        "Ảnh nền",
        upload_to="hero_slides/",
        help_text="Tỉ lệ khuyến nghị: 1920x1080. Có thể crop sau khi upload."
    )
    cropping = ImageRatioField('background', '1920x1080')
    
    # Buttons
    primary_button_text = models.CharField(
        max_length=50, 
        default="Đăng ký tham quan",
        verbose_name="Text nút chính"
    )
    primary_button_link = models.CharField(
        max_length=200,
        default="#contact", 
        verbose_name="Link nút chính"
    )
    
    secondary_button_text = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Text nút phụ"
    )
    secondary_button_link = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Link nút phụ"
    )
    
    # Thứ tự và hiển thị
    order = models.IntegerField(default=0, verbose_name="Thứ tự")
    is_active = models.BooleanField(default=True, verbose_name="Hiển thị")
    
    class Meta:
        verbose_name = "Hero Slide"
        verbose_name_plural = "Hero Slides"
        ordering = ['order']
    
    def __str__(self):
        return f"{self.title} (Order: {self.order})"
    
    # Helper method để tương thích với legacy code
    def get_cropped_image_url(self):
        """Trả về URL ảnh đã crop (tương thích với HeroSetting)"""
        if self.background and self.cropping:
            try:
                from easy_thumbnails.files import get_thumbnailer
                crop_coords = self.cropping
                if crop_coords and crop_coords.strip():
                    coords = crop_coords.split(',')
                    if len(coords) == 4:
                        x = int(round(float(coords[0])))
                        y = int(round(float(coords[1])))
                        w = int(round(float(coords[2])))
                        h = int(round(float(coords[3])))
                        box = (x, y, x + w, y + h)
                        
                        thumbnailer = get_thumbnailer(self.background)
                        cropped_image = thumbnailer.get_thumbnail({
                            'size': (1534, 512),
                            'crop': 'smart',
                            'quality': 95,
                            'box': box,
                        })
                        return cropped_image.url
                else:
                    return self.background.url
            except Exception as e:
                print(f"Error creating cropped thumbnail: {e}")
                return self.background.url if self.background else None
        return None


# ===== LEGACY MODEL (sẽ xóa sau khi migrate) =====
class HeroSetting(models.Model):
    """Legacy Hero Setting - SẼ BỊ XÓA sau khi migrate data"""
    background = ImageCropField(
        "Ảnh nền Hero",
        upload_to="hero_backgrounds/",
        null=True,
        blank=True,
    )
    cropping = ImageRatioField('background', '1534x512')

    def __str__(self):
        return "Hero background setting (Legacy - sẽ bị xóa)"
    
    class Meta:
        verbose_name = "Hero Setting (Legacy)"
        verbose_name_plural = "Hero Settings (Legacy)"

# ==================== PROGRAMS ====================
class Program(TimeStampedModel):
    """Chương trình học - Quản lý tại: Chương trình học → Programs"""
    name = models.CharField(max_length=200, verbose_name="Tên chương trình")
    description = models.TextField(verbose_name="Mô tả")
    age_range = models.CharField(max_length=50, verbose_name="Độ tuổi")
    
    # Ảnh chương trình
    image = FilerImageField(
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="program_images",
        verbose_name="Ảnh chương trình",
        help_text="Tỉ lệ khuyến nghị: 400x300"
    )
    
    # Icon (emoji hoặc text)
    icon = models.CharField(
        max_length=10,
        default="📚",
        verbose_name="Icon",
        help_text="Emoji hoặc ký tự đặc biệt"
    )
    
    # Thông tin thêm
    duration = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Thời gian học"
    )
    class_size = models.IntegerField(
        default=15,
        verbose_name="Sĩ số lớp"
    )
    
    # Thứ tự và hiển thị
    order = models.IntegerField(default=0, verbose_name="Thứ tự")
    is_featured = models.BooleanField(default=False, verbose_name="Nổi bật")
    is_active = models.BooleanField(default=True, verbose_name="Hiển thị")
    
    class Meta:
        verbose_name = "Chương trình học"
        verbose_name_plural = "Chương trình học"
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.age_range})"

# ==================== STAFF ====================
class Staff(TimeStampedModel):
    """Đội ngũ giáo viên - Quản lý tại: Thông tin cơ bản → Staff"""
    name = models.CharField(max_length=200, verbose_name="Họ tên")
    role = models.CharField(max_length=200, verbose_name="Chức vụ")
    description = models.TextField(verbose_name="Mô tả")
    
    # Ảnh giáo viên
    photo = FilerImageField(
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="staff_photos",
        verbose_name="Ảnh đại diện",
        help_text="Tỉ lệ khuyến nghị: vuông 400x400"
    )
    
    # Thông tin liên hệ
    email = models.EmailField(blank=True, verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Điện thoại")
    
    # Kinh nghiệm
    experience_years = models.IntegerField(
        default=0,
        verbose_name="Số năm kinh nghiệm"
    )
    education = models.TextField(
        blank=True,
        verbose_name="Học vấn"
    )
    specialization = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Chuyên môn"
    )
    
    # Thứ tự và hiển thị
    order = models.IntegerField(default=0, verbose_name="Thứ tự")
    is_featured = models.BooleanField(default=False, verbose_name="Nổi bật")
    is_active = models.BooleanField(default=True, verbose_name="Hiển thị")
    
    class Meta:
        verbose_name = "Giáo viên"
        verbose_name_plural = "Đội ngũ giáo viên"
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.name} - {self.role}"

# ==================== TESTIMONIALS ====================
class Testimonial(TimeStampedModel):
    """Đánh giá phụ huynh - Quản lý tại: Đánh giá phụ huynh → Testimonials"""
    parent_name = models.CharField(max_length=200, verbose_name="Tên phụ huynh")
    child_name = models.CharField(max_length=200, verbose_name="Tên con")
    child_class = models.CharField(max_length=100, verbose_name="Lớp")
    
    content = models.TextField(verbose_name="Nội dung đánh giá")
    rating = models.IntegerField(
        choices=[(i, f"{i} sao") for i in range(1, 6)],
        default=5,
        verbose_name="Đánh giá"
    )
    
    # Ảnh phụ huynh
    parent_photo = FilerImageField(
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="testimonial_photos",
        verbose_name="Ảnh phụ huynh",
        help_text="Tỉ lệ khuyến nghị: vuông 200x200"
    )
    
    # Thứ tự và hiển thị
    order = models.IntegerField(default=0, verbose_name="Thứ tự")
    is_featured = models.BooleanField(default=False, verbose_name="Nổi bật")
    is_active = models.BooleanField(default=True, verbose_name="Hiển thị")
    
    class Meta:
        verbose_name = "Đánh giá phụ huynh"
        verbose_name_plural = "Đánh giá phụ huynh"
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return f"{self.parent_name} - {self.child_name}"

# ==================== NEWS ====================
class News(TimeStampedModel, SEOModel):
    """Tin tức - Quản lý tại: Tin tức & Bài viết → News"""
    title = models.CharField(max_length=200, verbose_name="Tiêu đề")
    slug = models.SlugField(unique=True, verbose_name="Đường dẫn")
    excerpt = models.TextField(max_length=300, verbose_name="Mô tả ngắn")
    content = models.TextField(verbose_name="Nội dung")
    
    # Ảnh thumbnail
    thumbnail = FilerImageField(
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="news_thumbnails",
        verbose_name="Ảnh thumbnail",
        help_text="Tỉ lệ khuyến nghị: 400x300"
    )
    
    # Thông tin bài viết
    author = models.CharField(max_length=100, default="Admin", verbose_name="Tác giả")
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name="Ngày đăng")
    
    # Category
    category = models.CharField(
        max_length=50,
        choices=[
            ('news', 'Tin tức'),
            ('events', 'Sự kiện'),
            ('activities', 'Hoạt động'),
            ('announcements', 'Thông báo'),
        ],
        default='news',
        verbose_name="Danh mục"
    )
    
    # Thứ tự và hiển thị
    is_featured = models.BooleanField(default=False, verbose_name="Nổi bật")
    is_active = models.BooleanField(default=True, verbose_name="Hiển thị")
    
    class Meta:
        verbose_name = "Tin tức"
        verbose_name_plural = "Tin tức & Bài viết"
        ordering = ['-publish_date']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'slug': self.slug})

# ==================== CÁC MODEL CŨ (giữ nguyên) ====================
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
        related_name="school_logos",
        verbose_name="Logo trường"
    )
    hero_image = FilerImageField(
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL,
        related_name="school_hero_images",
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
        related_name="school_brochures",
        verbose_name="Brochure (PDF)"
    )
    
    class Meta:
        verbose_name = "Thông tin trường"
        verbose_name_plural = "Thông tin trường"
    
    def __str__(self):
        return self.name

class Gallery(TimeStampedModel):
    """Thư viện ảnh - Quản lý tại: Thông tin cơ bản → Gallery"""
    title = models.CharField(max_length=200, verbose_name="Tiêu đề")
    description = models.TextField(blank=True, verbose_name="Mô tả")
    image = FilerImageField(
        on_delete=models.CASCADE,
        related_name="gallery_images",
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
        related_name="achievement_images",
        verbose_name="Hình ảnh"
    )
    is_featured = models.BooleanField(default=False, verbose_name="Nổi bật")
    
    class Meta:
        verbose_name = "Thành tích"
        verbose_name_plural = "Thành tích & Giải thưởng"
        ordering = ['-year', 'title']
    
    def __str__(self):
        return f"{self.title} ({self.year})"

# Legacy model - giữ để tương thích
class HeroSetting(models.Model):
    """Legacy Hero Setting - sẽ được thay thế bởi HeroSlide"""
    background = ImageCropField(
        "Ảnh nền Hero",
        upload_to="hero_backgrounds/",
        null=True,
        blank=True,
    )
    cropping = ImageRatioField('background', '1534x512')

    def __str__(self):
        return "Hero background setting (Legacy)"
    
    class Meta:
        verbose_name = "Hero Setting (Cũ)"
        verbose_name_plural = "Hero Settings (Cũ)"