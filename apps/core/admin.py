from django.contrib import admin
from .models import SchoolInfo, Gallery, FAQ, Achievement
from .models import HeroSetting
from image_cropping import ImageCroppingMixin
from easy_thumbnails.files import get_thumbnailer
@admin.register(HeroSetting)
class HeroSettingAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['id', 'background', 'cropping']
    fields = ('background', 'cropping')
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        
        # Force clear cache cho image này
        if obj.background:
            try:
                thumbnailer = get_thumbnailer(obj.background)
                thumbnailer.delete_thumbnails()
                print(f"✅ Cleared thumbnails for: {obj.background.name}")
                print(f"✅ New crop coords: {obj.cropping}")
            except Exception as e:
                print(f"❌ Error clearing thumbnails: {e}")
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