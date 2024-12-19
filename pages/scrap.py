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


def get_driver():
    options = webdriver.ChromeOptions()
    
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    #options.add_argument(f"--window-size={width}x{height}")
    
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
all_img = driver.find_element(By.XPATH, '//h1')
st.write(all_img.text)
all_img = driver.find_elements(By.XPATH, '//h1')
st.write(all_img)

titulo = driver.find_elements(By.XPATH, '//form[@class="ob-card-body"]')
#titulo = driver.find_elements(By.XPATH, '//h1[contains(@class, "ob-card-body")]')
#titulo = driver.find_element(By.XPATH, '//h1[contains(@class, "ob-card-body")]')
st.code(titulo.text)
