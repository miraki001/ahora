import os
os.system("playwright install")
os.system("playwright install --with-deps chromium")
os.system("chromium install")
import streamlit as st
import asyncio
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

@st.cache_resource
def get_driver():
    return webdriver.Chrome(
        service=Service(
            ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
        ),
        options=options,
    )
options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--headless")

driver = get_driver()
sep = 'article'
dictitu = {'class':'inline-post-section section-full'}




with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()

    page.goto("https://www.growingproduce.com/fruits/grapes/")  # go to url
    #page.wait_for_selector("div[data-target=directory-first-item]")  # wait for content to load

    parsed = []
    soup = BeautifulSoup(page.content(), 'lxml' )
    #print('resultado')
    #print(soup)
    noticias = soup.find_all(sep,dictitu )
    
    for item in noticias:
            pp = item.find
