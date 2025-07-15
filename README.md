# Random Quote Generator on Django
_________________________________
## Описание проекта
Random Quote Generator - это веб-приложение на Django, которое позволяет пользователям:
* Получать случайные цитаты
* Оценивать цитаты (лайк/дизлайк)
* Просматривать топ-10 цитат по количеству лайков
* Видеть историю своих оценок (понравившиеся и непонравившиеся цитаты)
* Видеть историю своих просмотров
___
## Функциональность
* Добавление новых цитат в общий пул:
    * Исключаются дубликаты
    * У одного источника не больше трех цитат

* Генерация случайной цитаты с учетом ее веса(чем больше вес, тем выше шанс выпадения)

* Система просмотров, лайков и дизлайков для цитат

* Дополнительная страница с 10 самыми залайкаными цитатами

* Выборки
  * Список просмотренных цитат
  * Список понравившихся цитат
  * Список непонравившихся цитат
___
## Установка и запуск
```bash
git clone https://github.com/ivanbeginer/Django-Random-Quote-Generator
``` 
```bash
cd Django-Random-Quote-Generator 
```
```bash
python -m venv venv
```
```bash              
pip install -r requirements.txt
```
```bash 
python manage.py makemigrations
```
```bash
python manage.py migrate
```
```bash
python manage.py createsuperuser
```
```bash 
python manage.py load_data json_file.json
``` 
```bash 
python manage.py runserver
```
## URLS
* / - получить случайную цитату

* /like/<int:quote_id> - поставить лайк цитате

* /dislike/<int:quote_id> - поставить дизлайк цитате

* /trends - топ-10 цитат по лайкам

* /filter_by_likes - понравившиеся пользователю цитаты

* /filter_by_dislikes - непонравившиеся пользователю цитаты
* /history_of_views - просмотренные пользователем цитаты 
