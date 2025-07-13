from django.urls import path

from quotes.views import get_quote, views_logic, like_quote, dislike_quote

app_name = 'quotes'

urlpatterns = [
    path('get_quote/',views_logic,name='get_quote'),
    path('like_quote/<int:quote_id>',like_quote,name='like_quote'),
    path('dislike_quote/<int:quote_id>',dislike_quote,name='dislike_quote')
]
