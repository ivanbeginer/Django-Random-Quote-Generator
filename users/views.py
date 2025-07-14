from django.shortcuts import render

from users.models import User
import socket as sk

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
    user = User(ip_address=get_client_ip(request),watched_quotes={'watched_list':[]},liked_quotes={'liked_list':[]},disliked_quotes={'disliked_list':[]})
    user.save()
    return user
def get_user(request):
    user = User.objects.filter(ip_address=get_client_ip(request)).first()
    if not user:
        user=post_ip_address(request)
        return user
    return user