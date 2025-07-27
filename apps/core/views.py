from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods

@csrf_protect
@require_http_methods(["POST"])
def contact_form(request):
    """
    Xử lý form liên hệ từ trang chủ
    """
    if request.method == 'POST':
        parent_name = request.POST.get('parent_name', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip()
        child_age = request.POST.get('child_age', '').strip()
        message = request.POST.get('message', '').strip()
        
        # Validation
        if not parent_name or not phone:
            messages.error(request, 'Vui lòng điền đầy đủ họ tên và số điện thoại!')
            return redirect('/')
        
        try:
            # Import model ở đây để tránh circular import
            from apps.contacts.models import Contact
            
            # Lưu vào database
            Contact.objects.create(
                parent_name=parent_name,
                phone=phone,
                email=email if email else None,
                child_age=int(child_age) if child_age else None,
                message=message if message else None
            )
            
            messages.success(request, 'Cảm ơn bạn đã đăng ký! Chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất.')
            
        except Exception as e:
            messages.error(request, 'Có lỗi xảy ra khi gửi thông tin. Vui lòng thử lại sau!')
            print(f"Error saving contact: {e}")
        
        return redirect('/')
    
    return redirect('/')

def home_view(request):
    """
    View cho trang chủ với hero image đã crop
    """
    setting = HeroSetting.objects.first()
    hero_bg_url = None
    
    if setting and setting.background:
        try:
            crop_coords = setting.cropping
            if crop_coords and crop_coords.strip():
                coords = crop_coords.split(',')
                if len(coords) == 4:
                    x, y, w, h = map(int, coords)
                    box = (x, y, x + w, y + h)
                    
                    thumbnailer = get_thumbnailer(setting.background)
                    cropped_image = thumbnailer.get_thumbnail({
                        'size': (1534, 512),
                        'crop': 'smart',
                        'quality': 95,
                        'box': box,
                    })
                    hero_bg_url = cropped_image.url
                else:
                    hero_bg_url = setting.background.url
            else:
                hero_bg_url = setting.background.url
        except Exception as e:
            print(f"Error: {e}")
            hero_bg_url = setting.background.url
    
    context = {
        'hero_bg': hero_bg_url,
        'hero_setting': setting
    }
    
    return render(request, 'cms/home.html', context)
def kindergarten_home(request):
    """
    View cho trang chủ mầm non
    """
    context = {
        'page_title': 'Sunny Kids - Mầm Non Song Ngữ Quốc Tế',
        'meta_description': 'Trường mầm non song ngữ quốc tế hàng đầu với chương trình STEAM và Montessori',
    }
    return render(request, 'cms/home.html', context)