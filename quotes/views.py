from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.views import View

# Create your views here.

from quotes.models import Source,Quote
import random

from users.views import post_ip_address, get_user


def get_quote():
    weights_list = []
    text_list = []
    for quote in Quote.objects.all():
        quote.less_than_three()
        weights_list.append(quote.weight)
        text_list.append(quote)
    result = random.choices(text_list,weights=weights_list)
    return result[0]


def views_logic(request):

    user = get_user(request)

    watched_list = user.watched_quotes['watched_list']
    random_quote = get_quote()
    quote_id = random_quote.pk
    if quote_id not in watched_list:
        Quote.objects.filter(pk=quote_id).update(views = random_quote.views+1)
        random_quote.refresh_from_db()
        watched_list.append(quote_id)
        user.save()

    return render(request, 'quotes/quote.html', {'quote': random_quote})

def like_quote(request,quote_id):
    user = get_user(request)
    liked_list = user.liked_quotes['liked_list']
    disliked_list = user.disliked_quotes['disliked_list']
    watched_list = user.watched_quotes['watched_list']
    quote = Quote.objects.get(pk=quote_id)
    quote_id =quote.pk
    if quote_id in disliked_list:
        Quote.objects.filter(pk=quote_id).update(likes=quote.likes + 1,dislikes=quote.dislikes-1)
        quote.refresh_from_db()
        liked_list.append(quote_id)
        disliked_list.remove(quote_id)
        user.save()
    elif  quote_id not in liked_list and quote_id not in disliked_list:
        Quote.objects.filter(pk=quote_id).update(likes=quote.likes + 1)
        quote.refresh_from_db()
        liked_list.append(quote_id)
        user.save()
    elif quote_id in liked_list:
        Quote.objects.filter(pk=quote_id).update(likes=quote.likes - 1)
        quote.refresh_from_db()
        liked_list.remove(quote_id)
        user.save()
    return render(request, 'quotes/quote.html', {'quote': quote})

def dislike_quote(request,quote_id):
    user = get_user(request)
    liked_list = user.liked_quotes['liked_list']
    disliked_list = user.disliked_quotes['disliked_list']
    watched_list = user.watched_quotes['watched_list']
    quote = Quote.objects.get(pk=quote_id)
    quote_id = quote.pk
    if quote_id in liked_list:
        Quote.objects.filter(pk=quote_id).update(likes=quote.likes - 1, dislikes=quote.dislikes + 1)
        quote.refresh_from_db()
        liked_list.remove(quote_id)
        disliked_list.append(quote_id)
        user.save()
    elif quote_id not in disliked_list and not quote_id in liked_list:
        Quote.objects.filter(pk=quote_id).update(dislikes=quote.dislikes + 1)
        quote.refresh_from_db()
        disliked_list.append(quote_id)
        user.save()
    elif quote_id in disliked_list:
        Quote.objects.filter(pk=quote_id).update(dislikes=quote.dislikes - 1)
        quote.refresh_from_db()
        disliked_list.remove(quote_id)
        user.save()
    return render(request, 'quotes/quote.html', {'quote': quote})