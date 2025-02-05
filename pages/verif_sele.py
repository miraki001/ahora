import streamlit as st
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import requests
import shutil
import os

my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36  (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0 "



def get_driver():
    options = webdriver.ChromeOptions()
    
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    #options.add_argument("--no-sandbox")
    #options.add_argument("--disable-dev-shm-usage")
    #options.add_argument("--disable-features=NetworkService")
    #options.add_argument("--window-size=1920x1080")
    #options.add_argument("--disable-features=VizDisplayCompositor")
    #options.add_argument("--enable-javascript")
    
    #options.add_argument(f"--window-size={width}x{height}")
    #options.add_argument(f"--user-agent={my_user_agent}")
    
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    
    return webdriver.Chrome(service=service, options=options)

options = Options()
#options.add_argument('--disable-gpu')
#options.add_argument('--headless')
#options.add_argument("javascript.enabled", True)

driver = get_driver()
#url = 'https://pubs.acs.org/action/doSearch?field1=AllField&target=default&targetTab=std&text1=grape&startPage=&sortBy=Earliest'
url = 'https://www.sciencedirect.com/search/api?qs=grape&show=25&sortBy=date&t=b2bea8931965191740cebf4326a31a21a8486820cfa51ad697655fa41e8788844478bff3a9cec3d490b9736620833474ef4741e99f61f4c1feeb5fba67eb5267429071982f7331cea50cc6881d1cb5a31b09de97ae0cbfe16d3269a015400c4414cbf85106eba2be3cae9a054f2bb164&hostname=www.sciencedirect.com'


#options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')


driver.get(url)
#driver.execute_script("window.scrollTo(0,10000)")
sleep(2)

element = WebDriverWait(driver, 12).until(
            EC.presence_of_element_located((By.XPATH, "//button | //a | //div"))
)


st.write(element.get_attribute('innerHTML'))
st.write(element.get_attribute('outherHTML'))

#st.write(driver.get_attribute('innerHTML'))
#st.write(driver.get_attribute('outherHTML'))
#st.write(driver.page_source)
soup = BeautifulSoup(driver.page_source,"html.parser")
#st.write(soup)



st.title("PINTEREST IMAGE EXTRACTOR")

