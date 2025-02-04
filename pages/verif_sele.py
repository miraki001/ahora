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
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



url = 'https://pubs.acs.org/action/doSearch?field1=AllField&target=default&targetTab=std&text1=grape&startPage=&sortBy=Earliest'
    
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

