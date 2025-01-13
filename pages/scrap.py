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

my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"

fuente = st.session_state['vdescrip'] 
pais = st.session_state['vpais'] 
activa = st.session_state['vactiva'] 
sepa = st.session_state['vsepa'] 
vtitu = st.session_state['vtit'] 
vdet  = st.session_state['vdet'] 
vlink = st.session_state['vlink'] 



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

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')

driver = get_driver()



driver.get('https://www.observatoriova.com/')


driver.implicitly_wait(10) 
WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button | //a | //div"))
)
accept_text_variations = [
            "accept", "agree", "allow", "consent", "continue", "ok", "I agree", "got it"
    ]
        

sleep(1)


noticias = driver.find_elements(By.XPATH, sepa)
st.write(noticias)
for noticias in noticias:
    name = noticias.find_element(By.XPATH, vtitu).text
    #img = noticias.find_element(By.XPATH, ".//img").get_attribute("src")
    link = noticias.find_element(By.XPATH, vlink).get_attribute("href")
    det = noticias.find_element(By.XPATH, 'vdet).text
    #link1 = noticias.find_element(By.XPATH, ".//a/following::a").get_attribute("text")
    #name1 = noticias.find_element(By.CLASS_NAME, "excerpt mt-2").text
    st.write('Nombre ' + name)
    #st.write('imagen '+  img)
    st.write('link ' + link)
    #st.write('link 1 ' + link1)
    st.write(det)
    #st.write(name1)
                                                                                                               


