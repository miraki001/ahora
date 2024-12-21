import streamlit as st
import pandas as pd
import numpy as np
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

# Import selenium webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# Waiting
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


response = requests.get('https://www.vinetur.com/marketing/')
soup = BeautifulSoup(response.text, 'html.parser')
data = soup.find('div').text
st.write(data)
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
