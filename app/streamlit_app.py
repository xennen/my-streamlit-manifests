# Содержимое файла: streamlit_app.py

import streamlit as st

# Заголовок приложения
st.title('Мое первое приложение на Streamlit!')

# Текст
st.write('Это приложение развернуто в Kubernetes с помощью Argo CD. Ура!')

# Добавляем изображение
st.header('А вот и обещанная картинка:')

# st.image() - это команда для отображения картинки.
# Мы просто передаем ей URL изображения из интернета.
st.image('https://files.realpython.com/media/Pythons-Beautiful-Is-Better-Than-Ugly-Quote_Watermarked.a9f6719593b2.jpg')

st.balloons() # Небольшой приятный бонус :)