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


response = requests.get('https://www.vinetur.com/marketing/')
soup = BeautifulSoup(response.text, 'html.parser')
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
driver.implicitly_wait(10) 
WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button | //a | //div"))
)
accept_text_variations = [
            "accept", "agree", "allow", "consent", "continue", "ok", "I agree", "got it"
    ]
        

#sleep(1)

datos = driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/ul/li[contains(@span, 'display:block;font-size:12px;color:#757575;font-weight: 300;')]")
#datos = driver.find_elements(By.XPATH, "[contains(text(), 'background')]")
#datos =  driver.find_elements(By.tagName ,"li")


st.write(datos)
for datos in datos:
    try:
        name = datos.find_element(By.XPATH, ".//a").text
        link = datos.find_element(By.XPATH, ".//a").get_attribute("href")
        st.write(name)
        st.write(link)
    finally:
        st.write('none')

    

st.write('hasta aca')    



products = soup.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/ul/li")
st.write(products)
data = soup.find_all('a', 'li')

#data = soup.find('a')
st.write(data)
for link in soup.find_all('a'):
    st.write(link.get('href'))

st.write('despues')



options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
service = ChromeService(executable_path = r'./Driver/chromedriver')

url = "https://www.bayut.com/for-sale/property/abu-dhabi/"

header = st.container()
cont_url = st.container()
cont_properties = st.container()

@st.cache(suppress_st_warning=True)
def get_urls(filename):
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 1)
    st.write("Cache miss: Hey Arjun, Function ran even though @st.cache is defined.")
# try:    
    driver.get(url)
    driver.maximize_window() # For maximizing window
    
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "f1ab04e0"))).find_element(By.CLASS_NAME, "_44977ec6").click()

    locations = []

    listings = wait.until(EC.presence_of_element_located((By.CLASS_NAME , "b7a55500"))).find_elements(By.CLASS_NAME, "_1c4ffff0") # works
    for listing in listings:

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, '_7afabd84')))

        List_dict={
        'Name':listing.find_element(By.CLASS_NAME, '_9878d019').text,
        'URL':listing.find_element(By.CLASS_NAME, '_9878d019').get_attribute("href"),
        'Properties':listing.find_element(By.CLASS_NAME, '_1f6ed510').text
        }

        locations.append(List_dict)

    url_list = pd.DataFrame(locations, columns=['Name', 'URL', 'Properties'])
    url_list.to_csv(filename, mode='w', index=False, header=True)
    driver.close()
    driver.quit()
    return url_list # this is the addition for the streamlit app.

with cont_url:
    st.title('Properties for sale')

    url_list = get_urls('Location_URLs_.csv')
    st.write("Calling Arjun's get_urls() function.")
    option = st.selectbox('Select your asset:', url_list) 
    st.write('You selected:', option)
    st.table(url_list) # to see what the url_list is returning.
