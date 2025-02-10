import os
os.system("playwright install")
os.system("playwright install --with-deps chromium")
os.system("chromium install")
import streamlit as st
import asyncio
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

sep = 'article'
dictitu = {'class':'inline-post-section section-full'}


async def run_automation():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://docs.streamlit.io/')
        title = await page.title()
        await browser.close()
    return title

def run_async_function():
    return asyncio.run(run_automation())

if __name__ == "__main__":
    if st.button('Run Automation'):
        result_placeholder = st.empty()
        result_placeholder.text("Running automation...")
        result = run_async_function()
        result_placeholder.text(result)



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
