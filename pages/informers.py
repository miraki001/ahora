import streamlit as st
import pandas as pd
import numpy as np
import nltk
import wordcloud
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

st.set_page_config(
    page_title="Miraki",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded")
st.title("Miraki")
st.subheader("Plataforma de Vigilancia Tecnólogica e Inteligencia Competitiva")
st.image("ic_launcher44.png", width=100,)
