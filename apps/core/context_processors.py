from .models import HeroSlide, Program, Staff, Testimonial, News, Gallery, SchoolInfo
from easy_thumbnails.files import get_thumbnailer

def hero_settings(request):
    """
    Legacy context processor - backward compatibility
    Sử dụng HeroSlide đầu tiên làm hero_bg
    """
    try:
        # Lấy slide đầu tiên (active)
        first_slide = HeroSlide.objects.filter(is_active=True).order_by('order').first()
        
        if first_slide:
            hero_bg_url = first_slide.get_cropped_image_url()
            return {"hero_bg": hero_bg_url}
        else:
            return {"hero_bg": None}
            
    except Exception as e:
        print(f"Error in hero_settings context processor: {e}")
        return {"hero_bg": None}

def site_data(request):
    """
    Context processor cung cấp dữ liệu cho toàn bộ site
    """
    try:
        # Hero Slides (đã có crop functionality)
        hero_slides = HeroSlide.objects.filter(is_active=True).order_by('order')[:3]
        
        # Programs 
        programs = Program.objects.filter(is_active=True).order_by('order')[:6]
        featured_programs = Program.objects.filter(is_active=True, is_featured=True).order_by('order')[:3]
        
        # Staff
        staff_members = Staff.objects.filter(is_active=True).order_by('order')[:6]
        featured_staff = Staff.objects.filter(is_active=True, is_featured=True).order_by('order')[:3]
        
        # Testimonials
        testimonials = Testimonial.objects.filter(is_active=True).order_by('order')[:10]
        
        # News
        latest_news = News.objects.filter(is_active=True).order_by('-publish_date')[:3]
        featured_news = News.objects.filter(is_active=True, is_featured=True).order_by('-publish_date')[:6]
        
        # Gallery by categories
        gallery_classroom = Gallery.objects.filter(category='classroom').order_by('order')[:4]
        gallery_playground = Gallery.objects.filter(category='playground').order_by('order')[:4]
        gallery_activities = Gallery.objects.filter(category='activities').order_by('order')[:4]
        gallery_events = Gallery.objects.filter(category='events').order_by('order')[:4]
        
        # School info
        school_info = SchoolInfo.objects.first()
        
        return {
            # Hero Slides với crop functionality
            'hero_slides': hero_slides,
            
            # Programs
            'programs': programs,
            'featured_programs': featured_programs,
            
            # Staff
            'staff_members': staff_members,
            'featured_staff': featured_staff,
            
            # Testimonials
            'testimonials': testimonials,
            
            # News
            'latest_news': latest_news,
            'featured_news': featured_news,
            
            # Gallery
            'gallery_classroom': gallery_classroom,
            'gallery_playground': gallery_playground,
            'gallery_activities': gallery_activities,
            'gallery_events': gallery_events,
            
            # School
            'school_info': school_info,
        }
        
    except Exception as e:
        print(f"Error in site_data context processor: {e}")
def school_info(request):
    """
    Context processor thông tin trường (legacy)
    """
    return {
        'school_name': 'Sunny Kids',
        'school_phone': '028 1234 5678',
        'school_email': 'info@sunnykids.edu.vn',
        'school_address': '123 Đường ABC, Quận 1, TP.HCM'
    }