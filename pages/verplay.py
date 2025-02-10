import os
os.system("playwright install")
import streamlit as st
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

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
