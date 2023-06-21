## Proceso de Web Scraping - Obtención de Datos Adicionales



El siguiente código de Python realiza el proceso de web scraping para obtener datos adicionales de los cursos de Udemy. A continuación, se detallan los pasos del proceso:

1. Importación de bibliotecas necesarias:
   - `requests`: Para realizar solicitudes HTTP y obtener el contenido HTML de las páginas web.
   - `pandas`: Para manipular y analizar los datos en forma de DataFrames.
   - `BeautifulSoup`: Para analizar el contenido HTML y extraer la información deseada.

2. Lectura del archivo de datos iniciales:
   - Se lee el archivo "udemy_courses.csv" que contiene los datos iniciales de los cursos de Udemy.

3. Creación de la lista de URLs:
   - Se crea una lista de URLs a partir de la columna "url" del archivo de datos.

4. Inicialización de listas para almacenar los datos adicionales:
   - Se inicializan las listas "rating_list" y "language_list" para almacenar los datos de calificación e idioma de cada curso.

5. Iteración sobre las URLs y obtención de datos:
   - Se itera sobre cada URL de la lista y se realiza una solicitud GET para obtener el contenido HTML de la página web correspondiente al curso.
   - Se utiliza la biblioteca BeautifulSoup para analizar el contenido HTML y buscar los elementos que contienen la información deseada, como el idioma y la calificación del curso.
   - Si se encuentra la información, se agrega a las listas correspondientes. En caso contrario, se añade un valor "NoData".

6. Actualización del DataFrame con los datos adicionales:
   - Se agrega cada lista como una columna adicional en el DataFrame "udemy_2", correspondiendo a los datos de idioma y calificación de los cursos.

7. Guardado del DataFrame actualizado:
   - Se guarda el DataFrame actualizado en un nuevo archivo "udemy2.csv" para su posterior uso en el análisis y visualización.

Este proceso de web scraping permite obtener información adicional de los cursos de Udemy, como el idioma y la calificación, para enriquecer el análisis y la presentación en el dashboard interactivo. Los datos obtenidos se agregan al DataFrame y se guardan en un nuevo archivo para su posterior manipulación.
