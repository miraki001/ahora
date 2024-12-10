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



#default=["copyHtml5", "csvHtml5", "excelHtml5", "colvis"],
default=["copyHtml5", "csvHtml5", "excelHtml5"],

it_args = {}
it_args["buttons"] = default
it_args["select"] = True

  




conn = st.connection("postgresql", type="sql")
df1 = conn.query('select nuri,fuente,select_web selec,fecha,titulo,detalle from novedades order by nuri desc limit 2000;', ttl="0"),
df = df1[0]
#st.write(df1[0])

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
config = {
    'nuri' : st.column_config.NumberColumn('nuri', required=True),
    'fuente' : st.column_config.TextColumn('fuente'),
    'selec' : st.column_config.CheckboxColumn('selec'),
    'titulo' : st.column_config.TextColumn('titulo',  width='large'),
    'detalle' : st.column_config.TextColumn('detalle', width='large')
    
}
result = st.data_editor(df, column_config = config, num_rows='dynamic')
edited_df = st.data_editor(df) # 👈 An editable dataframe


interactive_table(df1[0],
                  caption='Countries',
                  select=True,
                  selected_rows=[0, 1, 2, 99, 99],
                  buttons=['copyHtml5', 'csvHtml5', 'excelHtml5', 'colvis'])

t = interactive_table(df1[0], **it_args )

df = df[pd.notnull(df['titulo'])]

df['fecha'] = pd.to_datetime(df.fecha, format='%Y-%m-%d')
fig = plt.figure()
ax = df.groupby(df.fecha.dt.year)['titulo'].count().plot(kind='bar', figsize=(12, 6))
ax.set(xlabel='Año', ylabel='Number of Articles', title="Articles Published Every Year")
plt.show()
st.pyplot(fig)

fig1 = plt.figure()
ax = df.groupby(df.fecha.dt.month)['titulo'].count().plot(kind='bar')
months = ['JAN',  'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
#ax.set_xticklabels(months)
ax.set(xlabel='Month', ylabel='Number of Articles', title="Articles Published Every Month")
plt.show()
st.pyplot(fig1)

fig2 = plt.figure()
nltk.download('stopwords')
stop_words = stopwords.words('english')
stopword_es = nltk.corpus.stopwords.words('spanish')
stop_words = stop_words + stopword_es

def cleaning(df, stop_words):
    df['titulo'] = df['titulo'].apply(lambda x:' '.join(x.lower() for x in x.split()))
    # Replacing the digits/numbers
    df['titulo'] = df['titulo'].str.replace('^\d+\s|\s\d+\s|\s\d+$', '')
    # Removing stop words
    df['titulo'] = df['titulo'].apply(lambda x:' '.join(x for x in x.split() if x not in stop_words))
    # Lemmatization
#    df['titulo'] = df['titulo'].apply(lambda x:' '.join([Word(x).lemmatize() for x in x.split()]))
    return df

data_v1 = cleaning(df, stop_words)
data_v1.head()


# Create and generate a word cloud image:
#wordcloud = WordCloud().generate(text)

common_words=''
for i in data_v1.titulo:  
    i = str(i)
    tokens = i.split()
    common_words += " ".join(tokens)+" "
wordcloud = wordcloud.WordCloud().generate(common_words)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()



