
# Используем официальный Python образ
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем всё приложение в контейнер
COPY . .

# Указываем порт, который будет использовать приложение (например, 8000)
EXPOSE 8000

# Определяем команду для запуска приложения
# Предполагаем, что ваше приложение запускается командой python app.py
CMD ["python", "app.py"]