import requests
import pandas as pd
from bs4 import BeautifulSoup

# Se lee el archivo "udemy_courses.csv" que contiene los datos iniciales de los cursos de Udemy
udemy_2 = pd.read_csv('data/udemy_courses.csv')

# Se crea una lista de URLs a partir de la columna "url" del archivo de datos
web_list = udemy_2['url'].to_list()

# Se inicializan las listas "rating_list" y "language_list" para almacenar los datos de calificación e idioma de cada curso
rating_list = []
language_list = []

# Se itera sobre cada URL de la lista y se realiza una solicitud GET para obtener el contenido HTML de la página web correspondiente al curso
for webpage in web_list:
    result = requests.get(webpage)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    # Se busca el elemento que contiene el idioma del curso y se almacena en la lista "language_list"
    language = soup.find('div', class_='clp-lead__element-item clp-lead__locale')
    if language is None:
        language_list.append('NoData')
    else:
        language_list.append(language.get_text().strip())

    # Se busca el elemento que contiene la calificación del curso y se almacena en la lista "rating_list"
    rating = soup.find('span', class_='ud-heading-sm star-rating-module--rating-number--2xeHu')
    if rating is None:
        rating_list.append('NoData')
    else:
        rating_list.append(rating.get_text().strip())

# Se agregan las listas "language_list" y "rating_list" como columnas adicionales en el DataFrame "udemy_2"
udemy_2['language'] = language_list
udemy_2['rating'] = rating_list

# Se guarda el DataFrame actualizado en un nuevo archivo "udemy2.csv"
udemy_2.to_csv('../data/udemy2.csv', index=False)
