import streamlit as st
import os
import sys
import time
import psutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from os.path import exists


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
driver.get("http://www.scrapingbee.com")
all_img = driver.find_elements(By.XPATH, "//img")
first_h1 = driver.find_elements(By.XPATH, "//h1")
st.write(len(first_h1))
for pp in len(first_h1):
    st.write(first_h1[pp].text)

# Get text of h1 tag
#first_h1_text = first_h1.text

# Get count of all_img and all_btn
all_img_count = len(all_img)


st.write(first_h1_text)
st.write(all_img_count)


driver.get('https://www.observatoriova.com/')
all_img = driver.find_elements(By.XPATH, "//h3")
st.write(all_img)
titulo = driver.find_elements(By.XPATH, '//h1[contains(@class, "ob-card-body")]')[0]
st.code(titulo)
