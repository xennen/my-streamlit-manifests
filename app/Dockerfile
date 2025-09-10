# Используем базовый образ Python
FROM python:3.9-slim

# Создаем рабочего пользователя
RUN useradd -ms /bin/bash appuser
USER appuser
WORKDIR /home/appuser

# Устанавливаем зависимости
RUN pip install streamlit

# КОПИРУЕМ ВАШ КОД ВНУТРЬ ОБРАЗА
# Копируем файл streamlit_app.py из текущей папки (где лежит Dockerfile)
# в рабочую директорию (/home/appuser) внутри контейнера.
COPY streamlit_app.py .

# Открываем порт, на котором работает Streamlit
EXPOSE 8501

# Команда для запуска вашего приложения
CMD ["streamlit", "run", "streamlit_app.py"]