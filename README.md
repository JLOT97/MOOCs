<div align="center">

# 📊🌐 Análisis de Mercado MOOC 💻📚


![Project Image](https://drive.google.com/uc?export=view&id=1MflVYobFu_JmMsBp4oI3cB3JvvGg7024)


</div>

Este proyecto tiene como objetivo realizar un análisis exhaustivo del mercado de MOOCs (Cursos Online Abiertos y Masivos) utilizando datos de la plataforma Udemy. A través del análisis de datos y la visualización de información relevante, buscamos comprender las tendencias, oportunidades y desafíos en el mercado de los cursos en línea.


## Estructura de archivos 📂📋

El proyecto incluye los siguientes archivos:



## 1. Datos 📊📂


- udemy_2.csv: Archivo CSV que contiene los datos limpios y preparados para el análisis. Este archivo se utiliza como base para el desarrollo del dashboard y otros análisis.

- udemy_final.csv: Archivo CSV que contiene los datos finales utilizados en el proyecto. Este archivo contiene las columnas adicionales y modificaciones realizadas durante el proceso de análisis.

- udemy_courses.csv: Archivo CSV original que contiene los datos brutos descargados de la plataforma Udemy. Este archivo se utiliza como punto de partida para el proceso de limpieza y preparación de datos.



## 2. Documentación 📄📝


- [Dashboard](Documents/dashboard_udemy.md): Documento que describe el diseño y la funcionalidad del dashboard creado en Power BI. Proporciona una visión general de las visualizaciones, gráficos y KPIs utilizados para analizar el mercado de MOOCs.

- [EDA](Documents/eda_udemy.md): Documento que detalla el proceso de Análisis Exploratorio de Datos (EDA) realizado en el proyecto. Describe las técnicas y visualizaciones utilizadas para comprender los patrones, tendencias y relaciones en los datos.

-  [Web Scraping](Documents/web_scraping.md): Documento que explica el proceso de web scraping utilizado para obtener datos adicionales de la plataforma Udemy. Describe las herramientas y bibliotecas utilizadas, así como los pasos seguidos para extraer la información relevante.



## 3. Scripts 📝🔧



- [EDA](scripts/udemy.ipynb) udemy.ipynb: Jupyter Notebook que contiene el código en Python utilizado para el análisis de datos, creación de visualizaciones y generación de métricas. Este notebook abarca todo el proceso desde la limpieza de datos hasta la creación del archivo udemy_final.csv.

- [Web Scraping](scripts/web_scrap_udemy.py): Script en Python que implementa el web scraping para obtener datos adicionales de la plataforma Udemy. Utiliza bibliotecas como requests, BeautifulSoup y pandas para extraer la información y guardarla en un archivo CSV.

- [Dashboard](proyecto2.2.pbix): Archivo de Power BI que contiene el dashboard interactivo desarrollado para analizar el mercado de MOOCs. Este archivo se utiliza para explorar visualmente los datos y obtener información valiosa sobre el mercado de cursos en línea.



## 4. Dependencias 🛠️📦


El proyecto depende de las siguientes bibliotecas y herramientas:

- pandas
- numpy
- seaborn
- matplotlib
- requests
- BeautifulSoup
- Power BI

*Asegúrese de tener estas dependencias instaladas para ejecutar los scripts y utilizar el dashboard de Power BI.*



## 5. Licencia 📄🔐

Este proyecto se distribuye bajo la licencia GNU GENERAL PUBLIC LICENSE Version 2, junio de 1991. Consulta el archivo LICENSE para obtener más detalles.
