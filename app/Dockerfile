# Используем базовый образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем сначала файл с зависимостями (лучшая практика)
# В нашем случае зависимость одна - streamlit, поэтому этот шаг пока пропустим
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# Устанавливаем Streamlit напрямую
RUN pip install streamlit

# Копируем ВЕСЬ контент из папки, где лежит Dockerfile, в рабочую директорию /app
COPY . .

# Открываем порт
EXPOSE 8501

# Команда для запуска. Теперь мы точно знаем, что streamlit_app.py лежит в /app
CMD ["streamlit", "run", "streamlit_app.py"]