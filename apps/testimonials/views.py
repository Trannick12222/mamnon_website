from django.shortcuts import render

def testimonial_list(request):
    """Danh sách đánh giá"""
    return render(request, 'testimonials/list.html')