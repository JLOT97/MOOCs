# Análisis Exploratorio de Datos (EDA)

El análisis exploratorio de datos es una etapa fundamental en cualquier proyecto de análisis y visualización de datos. A continuación, se detallan los pasos realizados en el EDA para el proyecto de Udemy:

1. Importación de las librerías necesarias:
   - Se importan las librerías pandas, matplotlib.pyplot, seaborn, numpy y langdetect para realizar el análisis y visualización de los datos.

2. Carga de los datos desde el archivo CSV:
   - Se carga el archivo "udemy_2.csv" que contiene los datos previamente procesados.

3. Observación de la estructura de los datos:
   - Se muestran las primeras filas del DataFrame para obtener una vista previa de los datos.
   - Se utiliza el método `info()` para conocer la estructura del DataFrame y verificar los tipos de datos de cada columna.

4. Observación y manipulación de las columnas del DataFrame:
   4.1. Observación de todas las columnas:
   - Se muestran todas las columnas del DataFrame para tener una visión completa de las características de los cursos de Udemy.
   
   4.2. Observación y manipulación de la columna 'course_id':
   - Se verifica si hay duplicados en la columna 'course_id' y se eliminan si existen.
   
   4.3. Observación y manipulación de la columna 'language':
   - Se muestra la distribución de los valores en la columna 'language'.
   - Se utiliza la función `detect_language()` para detectar el idioma de los títulos de los cursos y reemplazar los valores 'NoData'.
   - Se crea un diccionario `language_mapping` para mapear las abreviaciones de idiomas a los nombres completos de los idiomas.
   - Se realiza la sustitución de las abreviaciones por los nombres completos de los idiomas en la columna 'language'.

5. Eliminación de columnas innecesarias:
   - Se elimina la columna 'url', ya que no es relevante para el análisis y visualización.

6. Observación de los valores nulos:
   - Se verifica si hay valores nulos en el DataFrame y se muestra la cantidad de valores nulos por columna.

7. Conversión de la columna 'published_timestamp' a tipo fecha:
   - Se convierte la columna 'published_timestamp' a tipo fecha y se extrae solo la fecha sin la hora.

8. Observación de una muestra de los datos actualizados:
   - Se muestran las primeras filas del DataFrame actualizado para verificar los cambios realizados.

9. Cambio de características de la columna 'rating':
   - Se cambia el tipo de dato de la columna 'rating' a string para reemplazar las comas.
   - Se reemplazan las comas por puntos en la columna 'rating'.
   - Se reemplazan los valores 'NoData' por NaN.
   - Se convierte la columna 'rating' a tipo flotante.
   - Se reemplazan los valores NaN por la media de la columna.

10. Visualización de la distribución de las variables objetivo del proyecto:
    10.1. Distribución del precio en relación a todos los cursos:
    - Se crea un histograma para visualizar la distribución de precios de los cursos.
    
    10.2. Distribución de los temas con respecto a todos los cursos:
    - Se utiliza un gráfico de barras para mostrar la distribución de los temas de los cursos.
    
    10.3. Distribución de los niveles de los cursos respecto a la cantidad total de cursos:
    - Se crea un gráfico de barras para visualizar la distribución de los niveles de los cursos.
    
    10.4. Distribución de los cursos entre pagos y gratis:
    - Se realiza una transformación en la columna 'is_paid' para reemplazar los valores booleanos por 'Pago' y 'Gratis'.
    - Se muestra la distribución de los tipos de cursos utilizando un gráfico de barras.
    
    10.5. Análisis de si los cursos más caros atraen menos suscriptores:
    - Se utiliza un gráfico de dispersión para visualizar la relación entre el precio y el número de suscriptores de los cursos.
    
    10.6. Análisis de si los cursos con más reseñas tienden a tener calificaciones más altas:
    - Se ordena el DataFrame por la columna 'rating'.
    - Se utiliza un gráfico de dispersión para analizar la relación entre el número de reseñas y la calificación de los cursos.
    
    10.7. Análisis de precio vs. número de reseñas:
    - Se utiliza un gráfico de dispersión para visualizar la relación entre el precio y el número de reseñas de los cursos.

11. Mapa de calor para observar correlaciones entre las variables:
    - Se seleccionan solo las columnas numéricas del DataFrame.
    - Se calcula la matriz de correlación y se muestra en un mapa de calor.

12. Nube de palabras con la columna 'course_title':
    - Se crea una nube de palabras utilizando los títulos de los cursos para obtener una visualización de los términos más frecuentes.

13. Análisis de posibles valores atípicos:
    - Se muestra una descripción estadística del DataFrame para observar los posibles valores atípicos.
    - Se identifica y muestra el posible valor atípico en la columna 'content_duration'.
    - Se utilizan diagramas de cajas para visualizar posibles valores atípicos en las columnas 'price' y 'content_duration'.

14. Tendencia del número de cursos publicados por año en Udemy:
    - Se extrae el año de la columna 'published_timestamp'.
    - Se agrupa por año y se cuenta el número de cursos publicados.
    - Se visualiza la tendencia del número de cursos publicados por año en un gráfico de líneas.

15. Tendencia del precio promedio de los cursos por año en Udemy:
    - Se calcula el precio promedio por año utilizando la columna 'price'.
    - Se visualiza la tendencia del precio promedio de los cursos por año en un gráfico de líneas.

16. Redondeo de las columnas 'content_duration' y 'rating':
    - Se convierten las columnas 'content_duration' y 'rating' a tipo float.
    - Se redondean los valores de ambas columnas a 2 decimales.

17. Guardado y exportación de los datos a un archivo CSV:
    - Se guarda el DataFrame actualizado en un archivo "udemy_final.csv" para su posterior uso en el proyecto.

Estos pasos de análisis exploratorio de datos proporcionan una visión completa de los datos de los cursos de Udemy, desde la carga y limpieza hasta la visualización de las variables objetivo y el análisis de tendencias.
