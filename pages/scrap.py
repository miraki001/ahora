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


def get_driver():
    options = webdriver.ChromeOptions()
    
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    #options.add_argument(f"--window-size={width}x{height}")
    options.add_argument(f"--user-agent={my_user_agent}")
    
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    
    return webdriver.Chrome(service=service, options=options)

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')

driver = get_driver()


"""
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
#st.write(all_img.text)
all_img = driver.find_elements(By.XPATH, '//h1')
#st.write(all_img)

titulo = driver.find_elements(By.XPATH, '//div[@class="ob-card-body"]')
link = driver.find_elements(By.XPATH, '/div[@class="ob-card-footer"]/a')
link2 = driver.find_elements(By.XPATH, '//*[@id="main"]/div/section[1]/div/div[3]/div/div[1]/div[2]/a')

imagen = driver.find_elements(By.XPATH, '/div[@class="icon-header"]')
noticias = driver.find_elements(By.XPATH, '//div[@class="d-flex flex-column justify-content-between h-100"]')

for noticias in noticias:
    name = noticias.find_element(By.XPATH, ".//h3").text
    img = noticias.find_element(By.XPATH, ".//img").get_attribute("src")
    link = noticias.find_element(By.XPATH, ".//a").get_attribute("href")
    link1 = noticias.find_element(By.XPATH, ".//a/following::a").get_attribute("href")
    st.write(name)
    st.write(img)
    st.write(link)
    st.write(link1)



driver.get('https://www.mdpi.com/search?q=enology&year_from=2024&year_to=2024&page_count=50&sort=pubdate&view=default')
driver.implicitly_wait(10) 
WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button | //a | //div"))
)
accept_text_variations = [
            "accept", "agree", "allow", "consent", "continue", "ok", "I agree", "got it"
    ]
        

sleep(1)

noticias = driver.find_elements(By.XPATH, '//div[@class="article-content"]')
st.write(noticias)
for noticias in noticias:
    name = noticias.find_element(By.XPATH, './/a[@class="title-link"]').text
    #img = noticias.find_element(By.XPATH, ".//img").get_attribute("src")
    link = noticias.find_element(By.XPATH, ".//a").get_attribute("href")
    link1 = noticias.find_element(By.XPATH, ".//a/following::a").get_attribute("href")
    st.write(name)
    #st.write(img)
    st.write(link)
    st.write(link1)
"""

driver.get('https://pubmed.ncbi.nlm.nih.gov/?term=wine&sort=date')
driver.implicitly_wait(10) 

"""
WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button | //a | //div"))
)

accept_text_variations = [
            "accept", "agree", "allow", "consent", "continue", "ok", "I agree", "got it"
    ]
        
"""
sleep(1)

noticias = driver.find_elements(By.XPATH, '//div[@class="docsum-wrap"]')
st.write(noticias)
for noticias in noticias:
    name = noticias.find_element(By.XPATH, './/a[@class="docsum-title"]').text
    #img = noticias.find_element(By.XPATH, ".//img").get_attribute("src")
    link = noticias.find_element(By.XPATH, ".//a").get_attribute("href")
    link1 = noticias.find_element(By.XPATH, ".//a/following::a").get_attribute("href")
    st.write(name)
    #st.write(img)
    st.write(link)
    st.write(link1)


driver.get('https://mundoagro.cl/noticias/')
driver.implicitly_wait(10) 

"""
WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button | //a | //div"))
)

accept_text_variations = [
            "accept", "agree", "allow", "consent", "continue", "ok", "I agree", "got it"
    ]
        
"""
sleep(1)

sepa = '//figure[@class="mb-15"]'

noticias = driver.find_elements(By.XPATH, sepa)
st.write(noticias)
for noticias in noticias:
    name = noticias.find_element(By.XPATH, './/h[@class="post-title font-weight-bold mb-10"]').text
    img = noticias.find_element(By.XPATH, ".//img").get_attribute("src")
    link = noticias.find_element(By.XPATH, ".//a").get_attribute("href")
    #link1 = noticias.find_element(By.XPATH, ".//a/following::a").get_attribute("href")
    st.write(name)
    st.write(img)
    st.write(link)
    #st.write(link1)



"""
st.write(link2[0].get_attribute("href"))
element_list = [] 
list_link = []
list_img = []
for i in range(len(noticias)): 
    element_list.append([noticias[i].text])
    list_link.append(noticias[i].get_attribute("href"))
    list_img.append(noticias[i].get_attribute("src"))


#st.write(link)
st.write(element_list)
st.write(list_link)
st.write(list_img)

for i in range(len(titulo)): 
    element_list.append([titulo[i].text])

st.write(element_list)

element_list = [] 

for i in range(len(link)): 
    element_list.append(link[i].get_attribute("href"))

st.write(element_list)
element_list = [] 
for i in range(len(link)): 
    element_list.append([link[i].text])

st.write(element_list)

element_list = [] 
for i in range(len(link2)): 
    element_list.append(link2[i].get_attribute("href"))

st.write(element_list)

element_list = [] 
for i in range(len(imagen)): 
    element_list.append(imagen[i].get_attribute("img"))

st.write(element_list)
"""
