from django.shortcuts import render

def news_list(request):
    """Danh sách tin tức"""
    return render(request, 'news/list.html')