from django.shortcuts import render
from django.http import JsonResponse

def contact_page(request):
    """Trang liên hệ"""
    return render(request, 'contacts/contact.html')

def contact_form(request):
    """Xử lý form liên hệ"""
    if request.method == 'POST':
        # Xử lý form ở đây
        return JsonResponse({'success': True, 'message': 'Cảm ơn bạn đã liên hệ!'})
    return JsonResponse({'success': False})