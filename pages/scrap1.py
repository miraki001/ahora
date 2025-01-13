import streamlit as st
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import csv
import subprocess
import sys
#from st_aggrid import AgGrid
import os
from bs4 import BeautifulSoup
import requests
import re

from array import array
import pandas as pd
from IPython.display import display
from datetime import datetime

import re

# Import selenium webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# Waiting
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#response = requests.get('https://www.vinetur.com/marketing/')
#soup = BeautifulSoup(response.text, 'html.parser')
#data = soup.find('div').text

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

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')

driver = get_driver()
driver.get('https://www.vinetur.com/marketing/')
driver.implicitly_wait(40) 
WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.XPATH, "//button | //a | //div"))
)
accept_text_variations = [
            "accept", "agree", "allow", "consent", "continue", "ok", "I agree", "got it"
    ]
        

#sleep(1)

#datos = driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/ul/li [not(contains(class, 'adsbygoogle'))]")
datos = driver.find_elements(By.XPATH, "//li/div")
#not [@class='adsbygoogle']")
#datos = driver.find_elements(By.XPATH, "[contains(text(), 'background')]")
#datos =  driver.find_elements(By.tagName ,"li")


#st.write(datos)
for datos in datos:
#    try:
        name = datos.find_element(By.XPATH, ".//a").text
        link = datos.find_element(By.XPATH, ".//a").get_attribute("href")
#        img = datos.find_element(By.XPATH, "li").value_of_css_property("background")
        
        img = datos.value_of_css_property("background")
        st.write(img)
        img = re.split('[()]',img)[3]
#        image_url = getCssValue('background')
#        img = datos.find_elements(By.CSS_SELECTOR, "background").value_of_css_property("background")
#         img = datos.find_element(By.XPATH, ximage).get_attribute("src")

#        soup = BeautifulSoup(datos)
#        div_style = soup.find('div')['style']
#        style = cssutils.parseStyle(div_style)
        url = ['background-image']
        st.write(name)
        st.write(link)
        st.write(img)
#    finally:
#        st.write('none')

    

st.write('hasta aca')    



driver.get('https://enolife.com.ar/es/category/fincas/')
datos = driver.find_elements(By.XPATH, "//ul/li/article[@class='item']")
st.write(datos)   
for datos in datos:
        name = datos.find_element(By.XPATH, ".//h2/a").text
        link = datos.find_element(By.XPATH, ".//a").get_attribute("href")
        #img = datos.find_element(By.XPATH, "//img").get_attribute("src")
        
        img = datos.getCssValue("background-image")
        st.write(img)
        #img = re.split('[()]',img)[2]
        st.write(name)
        st.write(link)
        st.write(img)

st.write('despues')
driver.close()

