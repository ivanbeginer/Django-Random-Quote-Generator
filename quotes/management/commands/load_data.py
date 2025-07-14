import json

from django.core.exceptions import ValidationError
from django.core.management import BaseCommand
from django.db import transaction




class Command(BaseCommand):
    help = 'Load quotes with validation (max 3 quotes per source)'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **options):
        try:
            with open(options['json_file'], 'r', encoding='utf-8') as f:
                data = json.load(f)

                source_counts = {}
                for item in data:
                    if item['model'] == 'quotes.quote':
                        source_id = item['fields']['source']
                        source_counts[source_id] = source_counts.get(source_id, 0) + 1

                '''Проверка существующих цитат'''
                from quotes.models import Quote
                for source_id in source_counts:
                    existing = Quote.objects.filter(source_id=source_id).count()
                    if existing + source_counts[source_id] > 3:
                        raise ValidationError(
                            f'Источник {source_id} превысит лимит в 3 цитаты '
                            f'(уже {existing}, пытаемся добавить {source_counts[source_id]})'
                        )

                '''Загрузка с валидацией каждого объекта'''
                with transaction.atomic():
                    for item in data:
                        if item['model']=='quotes.source':
                            from quotes.models import Source
                            source = Source(
                                id=item['pk'],
                                name=item['fields']['name'],
                                author=item['fields']['author'],
                                year = item['fields']['year'],
                                type = item['fields']['type']
                            )
                            source.save()
                        if item['model'] == 'quotes.quote':
                            from quotes.models import Quote
                            quote = Quote(
                                id=item['pk'],
                                text=item['fields']['text'],
                                source_id=item['fields']['source'],
                                views=item['fields'].get('views', 0),
                                likes=item['fields'].get('likes', 0),
                                dislikes=item['fields'].get('dislikes', 0)
                            )
                            quote.save()



            self.stdout.write(self.style.SUCCESS(f'Успешно загружено {len(data)} объектов'))

        except ValidationError as e:
            self.stdout.write(self.style.ERROR(f'Ошибка валидации: {e}'))






