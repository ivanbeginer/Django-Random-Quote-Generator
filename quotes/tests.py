from django.test import TestCase

from quotes.models import Source, Quote
from users.models import User


# Create your tests here.

class TestQuote(TestCase):

    def setUp(self):
        self.source = Source.objects.create(name='TestSource',author='TestAuthor',type='Book',year=2222)
        self.quote = Quote.objects.create(text = 'TestText',weight=5,source=self.source)

    def test_get_quote(self):
        response = self.client.get('')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.context['quote'].text,'TestText')

    def test_like_quote(self):
        response = self.client.get(f'/like_quote/{self.quote.pk}')
        self.assertEqual(response.status_code,200)
    def test_dislike_quote(self):
        response = self.client.get(f'/dislike_quote/{self.quote.pk}')
        self.assertEqual(response.status_code,200)

