from django.shortcuts import render

# Create your views here.

from users.models import User
from viewer.models import Viewer


# Create your views here.

def get_client_ip(request):
    """Получает ip пользователя"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def post_ip_address(request):
    """Добавляет пользователя по ip"""
    viewer = Viewer(ip_address=get_client_ip(request),watched_quotes={'watched_list':[]},liked_quotes={'liked_list':[]},disliked_quotes={'disliked_list':[]})
    viewer.save()
    return viewer
def get_viewer(request):
    viewer = Viewer.objects.filter(ip_address=get_client_ip(request)).first()
    if not viewer:
        viewer=post_ip_address(request)
        return viewer
    return viewer