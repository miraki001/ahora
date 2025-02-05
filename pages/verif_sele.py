import streamlit as st
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

import requests
import shutil
import os



def get_driver():
    options = webdriver.ChromeOptions()
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    return webdriver.Chrome(service=service, options=option)



#url = 'https://pubs.acs.org/action/doSearch?field1=AllField&target=default&targetTab=std&text1=grape&startPage=&sortBy=Earliest'
url = 'https://www.sciencedirect.com/search/api?qs=grape&show=25&sortBy=date&t=b2bea8931965191740cebf4326a31a21a8486820cfa51ad697655fa41e8788844478bff3a9cec3d490b9736620833474ef4741e99f61f4c1feeb5fba67eb5267429071982f7331cea50cc6881d1cb5a31b09de97ae0cbfe16d3269a015400c4414cbf85106eba2be3cae9a054f2bb164&hostname=www.sciencedirect.com'

browser = get_driver()
options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')


browser.get(url)
browser.execute_script("window.scrollTo(0,10000)")
sleep(2)
soup = BeautifulSoup(browser.page_source,"html.parser")
st.write(soup)



st.title("PINTEREST IMAGE EXTRACTOR")

