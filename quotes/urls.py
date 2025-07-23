from django.urls import path

from quotes.views import register_view, like_quote, dislike_quote, order_by_likes, add_quote
from quotes.filters import  filter_by_likes, filter_by_dislikes, history_of_views

app_name = 'quotes'

urlpatterns = [
    path('',register_view,name='get_quote'),
    path('like_quote/<int:quote_id>',like_quote,name='like_quote'),
    path('dislike_quote/<int:quote_id>',dislike_quote,name='dislike_quote'),
    path('trends/',order_by_likes,name='order_by_likes'),
    path('history_of_views/',history_of_views, name='history_of_views'),
    path('filter_by_likes/',filter_by_likes,name='filter_by_likes'),
    path('filter_by_dislikes/',filter_by_dislikes,name='filter_by_dislikes'),
    path('add_quote/',add_quote,name='add_quote')
]
