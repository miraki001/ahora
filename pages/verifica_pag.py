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

col1, col2 = st.columns(2)



if col1.button("Home"):
    st.switch_page("streamlit_app.py")
if col2.button("Fuentes"):
    st.switch_page("./pages/fuentes.py")

my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36  (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0 "

#Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0


separador = st.session_state['vsepa'] 
st.write(separador)
xtitulo = st.session_state['vtit'] 
xlink = st.session_state['vlink'] 
ximage = st.session_state['vimagen'] 
xdetalle = st.session_state['vdet'] 
pag = st.session_state['vfuente'] 

tnuri = st.session_state['vnuri']
url = st.session_state['vfuente']
st.write(url)



def get_driver():
    options = webdriver.ChromeOptions()
    
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-features=NetworkService")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-features=VizDisplayCompositor")
    
    #options.add_argument(f"--window-size={width}x{height}")
    options.add_argument(f"--user-agent={my_user_agent}")
    
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    
    return webdriver.Chrome(service=service, options=options)

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')

driver = get_driver()


driver.implicitly_wait(10)
driver.get(url)
driver.implicitly_wait(2) 

WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//button | //a | //div"))
)
accept_text_variations = [
            "accept", "agree", "allow", "consent", "continue", "ok", "I agree", "got it"
    ]
        

sleep(1)

noticias = driver.find_elements(By.XPATH, separador)
st.write(noticias)
for noticias in noticias:
    #name = noticias.find_element(By.XPATH, xtitulo).text
    name = noticias.find_element(By.XPATH, xtitulo).get_attribute("text")

    #img = noticias.find_element(By.XPATH, ximage).get_attribute("src")
    link = noticias.find_element(By.XPATH, xlink).get_attribute("href")
    detalle = noticias.find_element(By.XPATH, xdetalle).get_attribute("text")
    #link1 = noticias.find_element(By.XPATH, ".//a/following::a").get_attribute("href")
    st.write(name)
    #st.write(img)
    st.write(link)
    st.write(detalle)

