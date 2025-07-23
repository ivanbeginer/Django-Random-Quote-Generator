from django import forms

from quotes.models import Source


class AddQuoteForm(forms.Form):
    text = forms.CharField(label="Введите цитату")
    source = forms.ModelChoiceField(queryset=Source.objects.all(),label='Выберите источник')
    weight = forms.IntegerField(label='Введите вес, влияющий на показ цитаты')

