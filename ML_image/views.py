import os
import numpy as np
import tensorflow as tf
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from keras.models import load_model
from PIL import Image, ImageOps

# Загрузка модели
model = load_model("sports_balls_model.h5")
classes = ['Американский футбол', 'Бейсбольный мяч', 'Баскетбол мяч', 'Билярдный шар', 'Шар для Боулинга',
           'Мяч для крикета','Футтбольный мяч','Мяч для гольфа','Хокейный мяч','Шайба','Мяч для рэкби','Воланчик',
           'Мяч для наст. тениса','Мяч для тенниса','Волейбольный мяч']  # Определение классов для классификации изображений

def home_page(request):
    file_url = None  # Переменная для хранения URL загруженного файла
    if request.method == 'POST':
        file = request.FILES['myfile1']  # Получение файла из формы
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)  # Получение URL загруженного файла

        # Открытие и обработка изображения
        image = Image.open('media/' + filename)
        size = (150, 150)  # Размер в соответствии с моделью
        image = ImageOps.fit(image, size, Image.LANCZOS)

        # Преобразование в формат для предсказания
        img_array = tf.keras.utils.img_to_array(image)
        img_array = tf.expand_dims(img_array, 0)

        # Получение предсказаний
        predictions = model.predict(img_array).flatten()
        predicted_class_index = np.argmax(predictions)  # Получение индекса класса
        predicted_class = classes[predicted_class_index]  # Именование выданного класса

        # Подготовка вероятностей классов
        probabilities = {classes[i]: float(predictions[i]) for i in range(len(classes))}

        # Отображение результатов
        return render(request, 'result.html', {
            'predicted_class': predicted_class,
            'predictions': probabilities,
        })

    return render(request, 'index.html', {'file_url': file_url})  # Передача переменной file_url в шаблон
