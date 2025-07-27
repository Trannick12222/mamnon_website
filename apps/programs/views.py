from django.shortcuts import render

def program_list(request):
    """Danh sách chương trình học"""
    return render(request, 'programs/list.html')
