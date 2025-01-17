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

tnuri = st.session_state['vnuri']
vurl = st.session_state['vfuente']
st.write(vurl)
st.write(xtitulo)
st.write(xdetalle)
#vv =  "'" + vatrib1 + "': '" + vatrib2 + "'" 
#st.write(vv)
newv = {vatrib1:vatrib2}
#separador = 'div'
#st.write(newv)
        


#vv = vv.replace('"','')
#vatrib = {  vv }

#vatrib ={"class": "col-md-4 mb-4"}

#st.write(vatrib)


conn = st.connection("postgresql", type="sql")
vquery = 'select * from fuentes_py where nuri = ' + tnuri + ';'
df2 = conn.query(vquery, ttl="0"),
df3 = df2[0]
#st.write(df3['atributo1'])

url = vurl
response = requests.get(url)
html_content = response.content
tree = html.fromstring(html_content)
soup = BeautifulSoup(html_content, 'lxml')
#st.write('aca')

#noticias = soup.find_all(class_='col-md-4 mb-4')
if vatrib != '':
    noticias = soup.find_all(separador,newv)
if vatrib == '':    
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
