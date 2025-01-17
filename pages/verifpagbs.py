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
fuenteorg = st.session_state['vfuenteorg'] 
urllink = st.session_state['vurllink'] 
posjson = st.session_state['vposjson'] 



tnuri = st.session_state['vnuri']
vurl = st.session_state['vfuente']
st.write(vurl)
st.write(xtitulo)
st.write(xdetalle)
newv = {vatrib1:vatrib2}
        
if tipobusq== 'json':
    my_url = vurl

    cookies = {
        "Hm_lpvt_7cd4710f721b473263eed1f0840391b4": "1548175412",
        "Hm_lvt_7cd4710f721b473263eed1f0840391b4": "1548140525",
        "x5sec":"7b22617365727665722d6c617a6164613b32223a223832333339343739626466613939303562613535386138333266383365326132434c4b516e65494645495474764a322b706f6d6f6941453d227d", }

    ret = requests.get(my_url, cookies=cookies)
    page_soup = soup(ret.text, 'lxml')
    data = page_soup.select(separador)[posjson]
    ojson = json.loads(data.text)
    for product in ojson:
        st.write(product[xtitulo])

    

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
