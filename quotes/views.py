
from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.

from quotes.models import Quote
import random

from viewer.views import get_viewer, get_client_ip


def get_quote():
    """Получает рандомную цитату"""
    weights_list = []
    text_list = []
    for quote in Quote.objects.all():
        weights_list.append(quote.weight)
        text_list.append(quote)
    result = random.choices(text_list,weights=weights_list)
    return result[0]


def register_view(request):
    """Регистрерует просмотр цитаты зрителем"""
    viewer = get_viewer(request)
    liked_list = viewer.liked_quotes['liked_list']
    disliked_list = viewer.disliked_quotes['disliked_list']
    watched_list = viewer.watched_quotes['watched_list']
    random_quote = get_quote()
    quote_id = random_quote.pk
    if quote_id not in watched_list:
        Quote.objects.filter(pk=quote_id).update(views = random_quote.views+1)
        random_quote.refresh_from_db()
        watched_list.append(quote_id)
        viewer.save()

    return render(request, 'quotes/base.html', {'quote': random_quote,'liked_list':liked_list,'disliked_list':disliked_list})

def like_quote(request,quote_id):
    """Лайк цитаты"""
    viewer = get_viewer(request)
    liked_list = viewer.liked_quotes['liked_list']
    disliked_list = viewer.disliked_quotes['disliked_list']

    quote = Quote.objects.get(pk=quote_id)
    quote_id =quote.pk
    if quote_id in disliked_list:
        Quote.objects.filter(pk=quote_id).update(likes=quote.likes + 1,dislikes=quote.dislikes-1)
        quote.refresh_from_db()
        liked_list.append(quote_id)
        disliked_list.remove(quote_id)
        viewer.save()
    elif  quote_id not in liked_list and quote_id not in disliked_list:
        Quote.objects.filter(pk=quote_id).update(likes=quote.likes + 1)
        quote.refresh_from_db()
        liked_list.append(quote_id)
        viewer.save()
    elif quote_id in liked_list:
        Quote.objects.filter(pk=quote_id).update(likes=quote.likes - 1)
        quote.refresh_from_db()
        liked_list.remove(quote_id)
        viewer.save()
    return render(request, 'quotes/base.html', {'quote': quote,'liked_list':liked_list})

def dislike_quote(request,quote_id):
    """Дизлайк цитаты"""
    viewer = get_viewer(request)
    liked_list = viewer.liked_quotes['liked_list']
    disliked_list = viewer.disliked_quotes['disliked_list']

    quote = Quote.objects.get(pk=quote_id)
    quote_id = quote.pk
    if quote_id in liked_list:
        Quote.objects.filter(pk=quote_id).update(likes=quote.likes - 1, dislikes=quote.dislikes + 1)
        quote.refresh_from_db()
        liked_list.remove(quote_id)
        disliked_list.append(quote_id)
        viewer.save()
    elif quote_id not in disliked_list and not quote_id in liked_list:
        Quote.objects.filter(pk=quote_id).update(dislikes=quote.dislikes + 1)
        quote.refresh_from_db()
        disliked_list.append(quote_id)
        viewer.save()
    elif quote_id in disliked_list:
        Quote.objects.filter(pk=quote_id).update(dislikes=quote.dislikes - 1)
        quote.refresh_from_db()
        disliked_list.remove(quote_id)
        viewer.save()
    return render(request, 'quotes/base.html', {'quote': quote,'disliked_list':disliked_list})
def order_by_likes(request):
    """Сортирует цитаты по убыванию количества лайков"""
    quotes = Quote.objects.order_by('-likes')
    liked_quotes = []
    for quote in quotes:
        if quote.likes>0:
            liked_quotes.append(quote)


    paginator = Paginator(liked_quotes,10)
    page_obj = paginator.get_page(request.GET.get('page'))
    user = get_viewer(request)
    watched_list = user.watched_quotes['watched_list']
    for quote in page_obj:
        if quote.pk not in watched_list:
            watched_list.append(quote.pk)
            Quote.objects.filter(pk=quote.pk).update(views=quote.views+1)
            quote.refresh_from_db()
            user.save()

    return render(request,'quotes/trends.html',{'quotes':page_obj})

