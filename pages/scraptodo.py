import streamlit as st
import os
import sys
import psutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from os.path import exists
import csv
from time import sleep
import pandas as pd
import re
from streamlit_extras.image_in_tables import table_with_images
import streamlit.components.v1 as components
from streamlit_echarts import st_echarts
import base64
import psycopg2
from sqlalchemy import text

vsepa = ''
vtitu = ''
vdeta = ''
vlink = ''
vimag = ''
vnuri = 0
vfuente = ''
vurl = ''
ptitulo = ''
pdet = ''
plink = ''
pimg = ''


my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"

def get_driver():
    options = webdriver.ChromeOptions()
    
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    #options.add_argument(f"--window-size={width}x{height}")
    options.add_argument(f"--user-agent={my_user_agent}")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-features=NetworkService")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-features=VizDisplayCompositor")
    
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    
    return webdriver.Chrome(service=service, options=options)

def insertar():
    st.write('este el titulo')
    st.write(ptitulo)
    conn = st.connection("postgresql", type="sql")
    with conn.session as session:
        ingresar = "insert into novedades (nuri,fuente,titulo,detalle,link,tipo,imagen,fecha,proyecto_nuri,fuente_nuri,eje_nuri)"
        ingresar = ingresar + " values (nextval('novedades_seq'),:fuente,:titulo,:detalle,:link,'P',:imagen,current_date,1,:fuente_nuri,1); "
        session.execute(text(ingresar), {"fuente": vfuente,"titulo": ptitulo,"detalle": pdet,"link": plink, "imagen": pimg,"fuente_nuri": vnuri})
        session.commit()
        


def scrap():
    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')

    driver = get_driver()
    st.write(vurl)
    driver.get(vurl)


    driver.implicitly_wait(10) 
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button | //a | //div"))
    )
    accept_text_variations = [
            "accept", "agree", "allow", "consent", "continue", "ok", "I agree", "got it"
    ]
    sleep(1)
    noticias = driver.find_elements(By.XPATH, vsepa)
    #st.write(noticias)
    for noticias in noticias:
        titulo = noticias.find_element(By.XPATH, vtitu).get_attribute("text")
        if vimag == '//img':
            img = noticias.find_element(By.XPATH, vimag).get_attribute("src")
            st.write(img)
            pimg = img
    
        if vimag == 'background':
            img = noticias.value_of_css_property("background") 
            img = re.split('[()]',img)[3]
            st.write(img)
            pimg = img
        link = noticias.find_element(By.XPATH, vlink).get_attribute("href")
        detalle = noticias.find_element(By.XPATH, vdeta).text
        #link1 = noticias.find_element(By.XPATH, ".//a/following::a").get_attribute("href")
        st.write(titulo)
        #st.write(img)
        st.write(link)
        ptitulo = titulo
        pdet = detalle
        plink = link
        st.write('titulo1')
        st.write(ptitulo)
        conn = st.connection("postgresql", type="sql")
        with conn.session as session:
#            ingresar = "insert into novedades (nuri,fuente,titulo,detalle,link,tipo,imagen,fecha,proyecto_nuri,fuente_nuri,eje_nuri)"
#            ingresar = ingresar + " values (nextval('novedades_seq'),:fuente,:titulo,:detalle,:link,'P',:imagen,current_date,1,:fuente_nuri,1); "
#            session.execute(text(ingresar), {"fuente": vfuente,"titulo": ptitulo,"detalle": pdet,"link": plink, "imagen": pimg,"fuente_nuri": vnuri})
            ingresar = "insert into prueba (nuri, otro) "
            ingresar = ingresar + "values ( nextval('prueba_seq'), :valor)  ;"
            session.execute(text(ingresar),{"valor": 1})
            session.commit()







conn = st.connection("postgresql", type="sql")
qq = "select * from fuentes_py where proyecto_nuri = 1 and activa = 'S'  ;"
df1 = conn.query(qq, ttl="0"),
df = df1[0]
st.write(df)
st.write(len(df))



for i in range(len(df)):
  vsepa = df['separador'][i]
  vtitu = df['xpath_titulo'][i]
  vdeta = df['xpath_detalle'][i]
  vlink = df['xpath_link'][i]
  vimag = df['xpath_image'][i]
  vnuri = df['nuri'][i]
  vfuente = df['descrip'][i]
  vurl = df['fuente'][i]
  st.write(df['nuri'][i])
  scrap()  
