import streamlit as st

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options() 
options.add_argument("--headless=new")
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')

#driver = get_driver()
driver.get('http://example.com')

st.code(driver.page_source)
