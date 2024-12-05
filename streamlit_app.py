import streamlit as st
import pandas as pd
import numpy as np
import nltk
import itables.options as it_op
from itables.streamlit import interactive_table
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords




#default=["copyHtml5", "csvHtml5", "excelHtml5", "colvis"],
default=["copyHtml5", "csvHtml5", "excelHtml5"],

it_args = {}
it_args["buttons"] = default
it_args["select"] = True

  




conn = st.connection("postgresql", type="sql")
df1 = conn.query('select nuri,fuente,fecha,titulo,detalle from novedades order by nuri desc limit 2000;', ttl="0"),
df = df1[0]
st.write(df1[0])

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

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()


#stopwords = set(open('stopwords.txt').read().split(','))
#stopwords = get_stop_words('english')
stop_words = get_stop_words('english')



wc = WordCloud(stopwords=stop_words)
wordcloud = wc.generate(' '.join(df['titulo'].apply(str)))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
st.pyplot(fig2)



