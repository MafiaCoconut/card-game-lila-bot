FROM python:3.11-slim

# Обновление системы и установка зависимостей
RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get install -y curl gcc build-essential firefox-esr \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Установка зависимостей Python
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копирование приложения
COPY ./app /app
WORKDIR /app

# Запуск приложения
CMD ["python", "main.py"]

