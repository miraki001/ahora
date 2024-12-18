import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
import os
from time import sleep
import pandas as pd
import re
from streamlit_extras.image_in_tables import table_with_images
import streamlit.components.v1 as components
from streamlit_echarts import st_echarts
import base64

check = st.checkbox('Ver reporte')
if check:
    st.subheader('Reporte creado con datasets generados a partir de la recolección de datos')
    st.markdown(
        """
        <div style="position: relative; overflow: hidden; padding-top: 75%; height: 0;">
            <iframe src="https://app.powerbi.com/view?r=eyJrIjoiODNmNzQyMGYtZjk0Zi00ZTBiLWI2MGMtMzkyOGFkOTFmMTI2IiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9" 
                    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"></iframe>
        </div>
        """,
        unsafe_allow_html=True
    )

st.title("Aplicación de raspado web para productos en Mercado Libre")
producto = st.text_input("Ingresa el nombre del producto")
boton_ejecutar = None

if not producto:
    st.info("Ingrese el producto, presione intro y ejecute proceso de raspado") 
else:
    boton_ejecutar = st.button("Ejecutar")

if boton_ejecutar:

    #options = webdriver.ChromeOptions()
    
    #options.add_argument('--disable-gpu')
    #options.add_argument('--headless')
    #options.add_argument(f"--window-size={width}x{height}")
    
    #service = Service()
    #driver = webdriver.Chrome(service=service, options=options)
    
    #return webdriver.Chrome(service=service, options=options)

    

    # Configuración del driver de Selenium
    #chrome_path = '/chromedriver'
    opts = webdriver.ChromeOptions()
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')

    
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    
    # URL SEMILLA
    url_busqueda = f"https://listado.mercadolibre.com.ar/{producto.replace(' ', '-')}/"
    driver.get(url_busqueda)
    sleep(1)

    #Elija la cantidad máxima de paginaciones o configurelo en la interfaz como otra opción para el usuario
    PAGINACION_MAX = 3
    PAGINACION_ACTUAL = 1

    # Lógica de extracción de datos
    try:
        disclaimer = driver.find_element(By.XPATH, '//button[@data-testid="action:understood-button"]')
        disclaimer.click()
    except Exception as e:
        print(e)
        None

    # Crear archivo CSV y escribir encabezados
    with open('productos_streamlit.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Título', 'Precio', 'Descripcion', 'Imagen', 'URL', 'Vendedor', 'Valoración', 'Tabla']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        with st.spinner("Extrayendo datos..."):
            progress_bar = st.progress(0)

            while PAGINACION_MAX > PAGINACION_ACTUAL:
                links_productos = driver.find_elements(By.XPATH, '//a[@class="ui-search-item__group__element shops__items-group-details ui-search-link"]')
                links_de_la_pagina = [a_link.get_attribute("href") for a_link in links_productos]

                for link in links_de_la_pagina:
                    sleep(1)
                    try:
                        driver.get(link)
                        sleep(1)
                        #Aquí extraerá los elementos que crea convenientes, tenga en cuenta que si es una pagina variable como ésta, deberá mejorar la lógica para que no le arroje errores, éstos son para el ej.  
                        titulo = driver.find_element(By.XPATH, '//h1[contains(@class,"ui-pdp-title")]').text
                        precio_texto = driver.find_element(By.XPATH, '//span[contains(@class,"andes-money-amount ui-pdp-price__part andes-money-amount--cents-superscript andes-money-amount--compact")]').text
                        precio_numero = re.search(r'\d+', precio_texto).group()
                        descripcion = driver.find_element(By.XPATH, '//p[@class="ui-pdp-description__content"]').text
                        img = driver.find_element(By.XPATH, '//img[@class="ui-pdp-image ui-pdp-gallery__figure__image"]')
                        imagen = img.get_attribute('src')
                        link_producto = driver.current_url
                        valuacion = driver.find_element(By.XPATH, "//*[@id='reviews_capability_v3']/div/section/div/div[1]/article/div/div[1]/div[1]/p").text
                        vendedor = driver.find_element(By.XPATH, "//p[@class='ui-seller-info__status-info__title ui-pdp-seller__status-title']").text
                        ver_mas_caracteristicas = driver.find_element(By.XPATH, '//span[@class="ui-pdp-collapsable__action" and text()="Ver más características"]')
                        ver_mas_caracteristicas.click()
                        sleep(1)

                        contenedor = driver.find_element(By.CLASS_NAME, "ui-vpp-highlighted-specs__striped-specs")
                        tabla = contenedor.find_element(By.CLASS_NAME, "andes-table")
                        filas = tabla.find_elements(By.CLASS_NAME, "andes-table__row")

                        tabla_lista = []
                        for fila in filas:
                            columna = fila.find_element(By.CLASS_NAME, "andes-table__header").text
                            columna2 = fila.find_element(By.CLASS_NAME, "andes-table__column").text
                            registro_tabla = columna + ":" + columna2
                            tabla_lista.append(registro_tabla)
                            tabla_texto = ', '.join(tabla_lista)

                        #Imprimir resultados
                        print(titulo)
                        print(precio_numero)
                        print(descripcion)
                        print(imagen)
                        print(link_producto)
                        print(valuacion)
                        print(vendedor)
                        print(tabla_texto)
                            
                        # Guardar datos en el archivo CSV
                        writer.writerow({'Título': titulo,
                                        'Precio': precio_numero,
                                        'Descripcion': descripcion,
                                        'Imagen': imagen,
                                        'URL': link_producto,
                                        'Valoración': valuacion,
                                        'Vendedor': vendedor,
                                        'Tabla': tabla_texto
                                        })

                        driver.back()
                    except Exception as e:
                        print(e)
                        driver.back()

                try:
                    puedo_seguir_horizontal = driver.find_element(By.XPATH, '//span[text()="Siguiente"]')
                    puedo_seguir_horizontal.click()
                except:
                    break
                
                PAGINACION_ACTUAL += 1
                progress = PAGINACION_ACTUAL / PAGINACION_MAX
                progress_bar.progress(progress)

    # Cerrar el driver de Selenium
    driver.quit()
    st.success("Extracción de datos completa.")

# Leer el archivo CSV y realizar la visualización de la tabla y el gráfico
if os.path.exists('productos_streamlit.csv'):
    df = pd.read_csv("productos_streamlit.csv")
    
    if len(df) > 0:
        selected_columns = ["Título","Precio","Imagen","Tabla","URL"]
        new_df = df[selected_columns].copy()
        new_df["URL"] = new_df["URL"].apply(lambda url: f'<a href="{url}" target="_blank">Enlace</a>')

        st.subheader("Resultado de productos")
        # Filtrar por rango de precio
        price_range = st.slider("Filtrar por rango de precio", float(new_df["Precio"].min()), float(new_df["Precio"].max()), (float(new_df["Precio"].min()), float(new_df["Precio"].max())),step=10.0)
        filtered_df = new_df[(new_df["Precio"] >= price_range[0]) & (new_df["Precio"] <= price_range[1])]

        # Ordenar por la columna "Precio" de manera ascendente o descendente
        sort_order = st.radio("Ordenar gráfico por:", ["Ascendente", "Descendente"])
        if sort_order == "Ascendente":
            price_sorted = filtered_df.sort_values("Precio", ascending=True)
        else:
            price_sorted = filtered_df.sort_values("Precio", ascending=False)

        # Convertir la columna "Título" y "Precio" en listas
        titulos = price_sorted["Título"].tolist()
        precios = price_sorted["Precio"].tolist()
        promedio_precios = price_sorted["Precio"].mean()
        
        options = {
            "xAxis": {
                "type": "category",
                "data": titulos,
            },
            "yAxis": {"type": "value"},
            "tooltip": {"show": True},
            "sort": sort_order,
            "series": [
                {"name": "$ Precios",
                "data": precios, 
                "type": "bar",
                "tooltip": {"show": True},
                },
                {"name": "$ Promedio",
                "data": [promedio_precios] * len(titulos),
                 "type": "line",
                 "tooltip": {"show": True},
                },
            ],
            "legend": {"data": ["$ Precios", "$ Promedio"]},
            "toolbox": {
                "feature": {
                    "dataView": { "show": True, "readOnly": False },
                    "magicType": { "show": True, "type": ["line", "bar"] },
                    "dataZoom": { "show": True },
                    "restore": { "show": True },
                    "saveAsImage": { "show": True },
                    }
            },
            
        }
        st_echarts(options=options)
        
        price_sorted["Precio"] = price_sorted["Precio"].apply(lambda price: f"${price}")
        img = table_with_images(df=price_sorted, url_columns=("Imagen",))
        img = img.replace('<img', '<img width="200"')
        st.markdown(img, unsafe_allow_html=True)

        # Convertir el DataFrame a formato CSV
        csv_string = price_sorted.to_csv(index=False, sep=",")
        # Convertir el CSV a bytes
        csv_bytes = csv_string.encode()
        # Generar el enlace de descarga
        b64 = base64.b64encode(csv_bytes).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="resultados_productos.csv">Descargar tabla en CSV</a>'
        # Mostrar el enlace de descarga
        st.markdown(href, unsafe_allow_html=True)
    else:
        st.warning("No hay registros en el archivo CSV para mostrar.")
else:
    st.error("No hay resultados para mostrar aún.")
