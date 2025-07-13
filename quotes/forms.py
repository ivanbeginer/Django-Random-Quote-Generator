from django import forms

from quotes.models import Source


class QuoteFilterForm(forms.Form):
    source = forms.ModelChoiceField(queryset=Source.objects.all(),label='Источники',required=False)
    options = forms.ChoiceField(choices=[('liked','Понравившиеся'),('viewed','Просмотренные'),('popular','Популярные')],required=False,label='Критерии')

