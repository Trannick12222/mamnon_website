from django.contrib import admin
from .models import (
    SchoolInfo, Gallery, FAQ, Achievement, HeroSetting,
    HeroSlide, Program, Staff, Testimonial, News
)
from image_cropping import ImageCroppingMixin

# ==================== HERO SLIDES ====================
# ==================== HERO SLIDES (Updated with full crop functionality) ====================
@admin.register(HeroSlide)
class HeroSlideAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active', 'background_preview', 'created_at')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'subtitle')
    ordering = ('order',)
    
    fieldsets = (
        ('Nội dung', {
            'fields': ('title', 'subtitle')
        }),
        ('🖼️ Hình ảnh & Crop', {
            'fields': ('background', 'cropping'),
            'description': 'Upload ảnh nền và crop theo ý muốn. Tỉ lệ khuyến nghị: 1920x1080'
        }),
        ('🔗 Nút bấm', {
            'fields': (
                ('primary_button_text', 'primary_button_link'),
                ('secondary_button_text', 'secondary_button_link')
            ),
            'classes': ('collapse',)
        }),
        ('⚙️ Cài đặt', {
            'fields': ('order', 'is_active')
        }),
    )
    
    def background_preview(self, obj):
        """Hiển thị preview ảnh trong list view"""
        if obj.background:
            return f'<img src="{obj.background.url}" style="width: 50px; height: 30px; object-fit: cover; border-radius: 4px;">'
        return "Không có ảnh"
    background_preview.allow_tags = True
    background_preview.short_description = "Preview"
    
    def save_model(self, request, obj, form, change):
        """Clear thumbnails khi save để force regenerate cropped images"""
        super().save_model(request, obj, form, change)
        
        # Force clear cache cho image này
        if obj.background:
            try:
                from easy_thumbnails.files import get_thumbnailer
                thumbnailer = get_thumbnailer(obj.background)
                thumbnailer.delete_thumbnails()
                print(f"✅ Cleared thumbnails for: {obj.background.name}")
                print(f"✅ New crop coords: {obj.cropping}")
            except Exception as e:
                print(f"❌ Error clearing thumbnails: {e}")

# ==================== XÓA HERO SETTING ADMIN ====================
# COMMENT OUT hoặc XÓA đoạn này:
# @admin.register(HeroSetting)
# class HeroSettingAdmin(ImageCroppingMixin, admin.ModelAdmin):
#     list_display = ['id', 'background']
#     fields = ('background', 'cropping')
# ==================== PROGRAMS ====================
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'age_range', 'class_size', 'order', 'is_featured', 'is_active')
    list_editable = ('order', 'is_featured', 'is_active')
    list_filter = ('is_featured', 'is_active', 'created_at')
    search_fields = ('name', 'description', 'age_range')
    ordering = ('order', 'name')
    
    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('name', 'description', 'age_range', 'icon')
        }),
        ('Hình ảnh', {
            'fields': ('image',),
            'description': 'Upload ảnh đại diện cho chương trình học'
        }),
        ('Chi tiết', {
            'fields': ('duration', 'class_size')
        }),
        ('Cài đặt', {
            'fields': ('order', 'is_featured', 'is_active')
        }),
    )

# ==================== STAFF ====================
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'experience_years', 'order', 'is_featured', 'is_active')
    list_editable = ('order', 'is_featured', 'is_active')
    list_filter = ('role', 'is_featured', 'is_active', 'experience_years')
    search_fields = ('name', 'role', 'description', 'specialization')
    ordering = ('order', 'name')
    
    fieldsets = (
        ('Thông tin cá nhân', {
            'fields': ('name', 'role', 'description')
        }),
        ('Ảnh đại diện', {
            'fields': ('photo',),
            'description': 'Upload ảnh đại diện của giáo viên'
        }),
        ('Liên hệ', {
            'fields': ('email', 'phone')
        }),
        ('Trình độ', {
            'fields': ('experience_years', 'education', 'specialization')
        }),
        ('Cài đặt', {
            'fields': ('order', 'is_featured', 'is_active')
        }),
    )

# ==================== TESTIMONIALS ====================
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('parent_name', 'child_name', 'child_class', 'rating', 'order', 'is_featured', 'is_active')
    list_editable = ('order', 'is_featured', 'is_active')
    list_filter = ('rating', 'child_class', 'is_featured', 'is_active', 'created_at')
    search_fields = ('parent_name', 'child_name', 'content')
    ordering = ('order', '-created_at')
    
    fieldsets = (
        ('Thông tin phụ huynh', {
            'fields': ('parent_name', 'child_name', 'child_class')
        }),
        ('Ảnh phụ huynh', {
            'fields': ('parent_photo',),
            'description': 'Upload ảnh đại diện của phụ huynh'
        }),
        ('Đánh giá', {
            'fields': ('content', 'rating')
        }),
        ('Cài đặt', {
            'fields': ('order', 'is_featured', 'is_active')
        }),
    )

# ==================== NEWS ====================
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'publish_date', 'is_featured', 'is_active')
    list_editable = ('is_featured', 'is_active')
    list_filter = ('category', 'is_featured', 'is_active', 'publish_date')
    search_fields = ('title', 'excerpt', 'content')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-publish_date',)
    
    fieldsets = (
        ('Nội dung bài viết', {
            'fields': ('title', 'slug', 'excerpt', 'content')
        }),
        ('Hình ảnh', {
            'fields': ('thumbnail',),
            'description': 'Upload ảnh thumbnail cho bài viết'
        }),
        ('Thông tin bài viết', {
            'fields': ('category', 'author')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
        ('Cài đặt', {
            'fields': ('is_featured', 'is_active')
        }),
    )


@admin.register(SchoolInfo)
class SchoolInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created_at')
    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('name', 'slogan', 'description')
        }),
        ('Thông tin liên hệ', {
            'fields': ('address', 'phone', 'email', 'website')
        }),
        ('Giờ hoạt động', {
            'fields': ('working_hours', 'working_days')
        }),
        ('Hình ảnh & Tài liệu', {
            'fields': ('logo', 'hero_image', 'brochure')
        }),
        ('Mạng xã hội', {
            'fields': ('facebook_url', 'youtube_url', 'instagram_url')
        }),
    )

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'order', 'created_at')
    list_filter = ('category', 'is_featured')
    list_editable = ('is_featured', 'order')
    search_fields = ('title', 'description')

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'is_active', 'order')
    list_filter = ('category', 'is_active')
    list_editable = ('is_active', 'order')
    search_fields = ('question', 'answer')

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'is_featured', 'created_at')
    list_filter = ('year', 'is_featured')
    list_editable = ('is_featured',)
    search_fields = ('title', 'description')