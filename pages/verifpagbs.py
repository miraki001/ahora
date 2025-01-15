import streamlit as st
import os
import sys
import psutil
import requests
from bs4 import BeautifulSoup
from lxml import html



url = 'https://www.thedrinksbusiness.com/tag/wine/'
response = requests.get(url)
html_content = response.content
tree = html.fromstring(html_content)
soup = BeautifulSoup(html_content, 'lxml')

noticias = soup.find_all('div', class_='col-md-4 mb-4')
for p in noticias:
    title = p.find('a')
    href = title.get("href")
    tite = p.find('h2').get_text()
    det = p.find('h2').get_text()

    #p.attrs['a']
    print(href)
    print(tite)
    print(det)
