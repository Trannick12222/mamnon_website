from django.shortcuts import render
from .models import ClassType, Teacher, Class

def class_list(request):
    """Danh sách lớp học"""
    classes = ClassType.objects.filter(is_active=True)
    return render(request, 'schools/class_list.html', {'classes': classes})

def teacher_list(request):
    """Danh sách giáo viên"""
    teachers = Teacher.objects.filter(is_active=True)
    return render(request, 'schools/teacher_list.html', {'teachers': teachers})