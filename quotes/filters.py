from django.shortcuts import render


from quotes.models import Quote
from users.views import get_user


def filter_by_likes(request):
    """Показывает понравившиеся цитаты"""
    user = get_user(request)
    quotes = Quote.objects.filter(id__in=user.liked_quotes['liked_list'])

    return render(request,'quotes/filters.html',{'quotes':quotes})

def history_of_views(request):
    """Показывает историю просмотров"""
    user = get_user(request)
    quotes = Quote.objects.filter(id__in=user.watched_quotes['watched_list'])
    return render(request,'quotes/filters.html',{'quotes':quotes})

def filter_by_dislikes(request):
    """Показывает непонравившиеся цитаты"""
    user=get_user(request)
    quotes = Quote.objects.filter(id__in=user.disliked_quotes['disliked_list'])
    return render(request,'quotes/filters.html',{'quotes':quotes})