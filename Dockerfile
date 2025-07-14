# Базовый образ
FROM python:3.12

# Установка зависимостей
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Рабочая директория
WORKDIR /app

# Копирование зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование проекта
COPY src/ .

# Команда запуска
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "DjangoRandomQuoteGenerator.wsgi:application"]