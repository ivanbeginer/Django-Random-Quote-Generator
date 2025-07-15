from django.shortcuts import render


from quotes.models import Quote
from viewer.views import get_viewer


def filter_by_likes(request):
    """Показывает понравившиеся цитаты"""
    viewer = get_viewer(request)
    quotes = Quote.objects.filter(id__in=viewer.liked_quotes['liked_list'])

    return render(request,'quotes/filters.html',{'quotes':quotes})

def history_of_views(request):
    """Показывает историю просмотров"""
    viewer = get_viewer(request)
    quotes = Quote.objects.filter(id__in=viewer.watched_quotes['watched_list'])
    return render(request,'quotes/filters.html',{'quotes':quotes})

def filter_by_dislikes(request):
    """Показывает непонравившиеся цитаты"""
    viewer=get_viewer(request)
    quotes = Quote.objects.filter(id__in=viewer.disliked_quotes['disliked_list'])
    return render(request,'quotes/filters.html',{'quotes':quotes})
