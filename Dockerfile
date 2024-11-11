# Базовый образ Python
FROM python:3.10-slim

# Установка необходимых библиотек для Tkinter
RUN apt-get update && \
    apt-get install -y python3-tk libx11-6 tk8.6-dev tcl8.6-dev libxrender1 libxtst6 libxi6 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Установка Python-зависимостей
RUN pip install numpy matplotlib

# Копирование и установка приложения
WORKDIR /app
COPY app/app.py .

# Запуск приложения
CMD ["python3", "app.py"]
