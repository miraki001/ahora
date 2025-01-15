import streamlit as st
import os
import re
import sys
import psutil
import requests
from bs4 import BeautifulSoup
from lxml import html

col1, col2 = st.columns(2)



if col1.button("Home"):
    st.switch_page("streamlit_app.py")
if col2.button("Fuentes"):
    st.switch_page("./pages/fuentes.py")


separador = st.session_state['vsepa'] 
st.write(separador)
xtitulo = st.session_state['vtit'] 
xlink = st.session_state['vlink'] 
ximage = st.session_state['vimagen'] 
xdetalle = st.session_state['vdet'] 
pag = st.session_state['vfuente'] 
separador = "class_='col-md-4 mb-4'"
#separdor = str(separador)
st.write(separador)

tnuri = st.session_state['vnuri']
vurl = st.session_state['vfuente']
st.write(vurl)
st.write(xtitulo)
st.write(xdetalle)


url = vurl
response = requests.get(url)
html_content = response.content
tree = html.fromstring(html_content)
soup = BeautifulSoup(html_content, 'lxml')
st.write('aca')

#noticias = soup.find_all(class_='col-md-4 mb-4')
noticias = soup.find_all(attrs=separador)
for p in noticias:
    title = p.find(xlink)
    href = title.get("href")
    title = p.find(xtitulo).get_text()
    det = p.find(xdetalle).get_text()

    st.write(href)
    st.write(title)
    #st.write(det)
