import streamlit as st
import pandas as pd
import numpy as np
import nltk
import wordcloud
#import pages as pg
import itables.options as it_op
from itables.streamlit import interactive_table
import matplotlib.pyplot as plt
import re
#from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.stem.porter import * 
from gensim.models import word2vec 
from sklearn.manifold import TSNE 
from nltk.tokenize import word_tokenize
stemmer = PorterStemmer()  
from streamlit_navigation_bar import st_navbar
 

st.set_page_config(initial_sidebar_state="expanded")








#default=["copyHtml5", "csvHtml5", "excelHtml5", "colvis"],
default=["copyHtml5", "csvHtml5", "excelHtml5"],




it_args = {}
it_args["buttons"] = default
it_args["select"] = True

  




conn = st.connection("postgresql", type="sql")
df1 = conn.query('select nuri,fuente,select_web selec,fecha,titulo,detalle,imagen,link from novedades order by nuri desc limit 2000;', ttl="0"),
df = df1[0]
#st.write(df1[0])

col = st.columns((1.5, 4.5, 2,2), gap='medium')

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color:#73a37;
    color:#e69d87;
}
div.stButton > button:hover {
    background-color:#759aa0;
    color:#8dc1a9;
    }
</style>""", unsafe_allow_html=True)

def informers():
    st.title("Page 2")

with col[0]:
    st.button("Editar", type="primary" )
with col[1]:
    st.button("Seleccionar", type="primary")
with col[2]:
    st.button("Quitar Seleccion", type="primary")
with col[3]:
    st.button("Informes", type="primary")


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
config = {
    'nuri' : st.column_config.NumberColumn('nuri', required=True),
    'fuente' : st.column_config.TextColumn('fuente'),
    'selec' : st.column_config.CheckboxColumn('selec'),
    'titulo' : st.column_config.TextColumn('titulo',  width='large'),
    'detalle' : st.column_config.TextColumn('detalle', width='large'),
    'imagen' : st.column_config.ImageColumn('imagen'),
    'link' : st.column_config.LinkColumn('link'),
    
}
result = st.data_editor(df, column_config = config, num_rows='dynamic')
edited_df = st.data_editor(df) # 👈 An editable dataframe


