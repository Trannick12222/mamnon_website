from .models import HeroSetting
from easy_thumbnails.files import get_thumbnailer
import hashlib

def hero_settings(request):
    """
    Context processor để thêm ảnh hero đã crop vào template
    """
    try:
        setting = HeroSetting.objects.first()
        hero_bg_url = None
        
        if setting and setting.background:
            try:
                crop_coords = setting.cropping
                
                if crop_coords and crop_coords.strip():
                    coords = crop_coords.split(',')
                    if len(coords) == 4:
                        # FIX: Parse float rồi round về int
                        x = int(round(float(coords[0])))
                        y = int(round(float(coords[1])))
                        w = int(round(float(coords[2])))
                        h = int(round(float(coords[3])))
                        
                        box = (x, y, x + w, y + h)
                        print(f"✅ Crop coords: {crop_coords}")
                        print(f"✅ Processed box: {box}")
                        
                        # Tạo unique cache key
                        cache_key = hashlib.md5(f"{setting.background.name}_{crop_coords}".encode()).hexdigest()[:8]
                        
                        thumbnailer = get_thumbnailer(setting.background)
                        cropped_image = thumbnailer.get_thumbnail({
                            'size': (1534, 512),
                            'crop': 'smart',
                            'quality': 95,
                            'box': box,
                            'detail': True,
                            'upscale': True,
                            'subdir': f'hero_crops_{cache_key}',
                        })
                        hero_bg_url = cropped_image.url
                        print(f"✅ Using cropped image: {hero_bg_url}")
                    else:
                        hero_bg_url = setting.background.url
                        print(f"⚠️ Invalid crop coords count, using original")
                else:
                    hero_bg_url = setting.background.url
                    print(f"⚠️ No crop data, using original")
                    
            except ValueError as e:
                print(f"❌ ValueError parsing coords: {e}")
                hero_bg_url = setting.background.url
            except Exception as e:
                print(f"❌ Error creating thumbnail: {e}")
                hero_bg_url = setting.background.url
        
        return {"hero_bg": hero_bg_url}
        
    except Exception as e:
        print(f"❌ Error in context processor: {e}")
        return {"hero_bg": None}

def school_info(request):
    return {
        'school_name': 'Sunny Kids',
        'school_phone': '028 1234 5678',
        'school_email': 'info@sunnykids.edu.vn',
        'school_address': '123 Đường ABC, Quận 1, TP.HCM'
    }