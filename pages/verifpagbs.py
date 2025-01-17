import streamlit as st
import os
import re
import sys
import psutil
import requests
from bs4 import BeautifulSoup
from lxml import html
import psycopg2
from sqlalchemy import text

col1, col2 = st.columns(2)



if col1.button("Home"):
    st.switch_page("streamlit_app.py")
if col2.button("Fuentes"):
    st.switch_page("./pages/fuentes.py")


separador = st.session_state['vsepa'] 
vatrib1 = st.session_state['vatributo1'] 
vatrib2 = st.session_state['vatributo2'] 
st.write(separador)
xtitulo = st.session_state['vtit'] 
xlink = st.session_state['vlink'] 
ximage = st.session_state['vimagen'] 
xdetalle = st.session_state['vdet'] 
pag = st.session_state['vfuente'] 
tipobusq = st.session_state['vtipobus'] 

tnuri = st.session_state['vnuri']
vurl = st.session_state['vfuente']
st.write(vurl)
st.write(xtitulo)
st.write(xdetalle)
newv = {vatrib1:vatrib2}
        
if tipobusq== 'json':


    

if tipobus != 'json':
    url = vurl
    response = requests.get(url)
    html_content = response.content
    tree = html.fromstring(html_content)
    soup = BeautifulSoup(html_content, 'lxml')
    if vatrib1 != '':
        noticias = soup.find_all(separador,newv)
    if vatrib1 == '':    
        noticias = soup.find_all(separador)
    for p in noticias:
        title = p.find(xlink)
        href = title.get("href")
        title = p.find(xtitulo).get_text()
        det = p.find(xdetalle).get_text()
        if ximage !='none':
            img = p.find(ximage).get('data-src')
            st.write(img)
        st.write(href)
        st.write(title)
        st.write(det)
