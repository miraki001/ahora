import streamlit as st
import pandas as pd
import numpy as np


  col1 = st.columns((1.5, 14.5, 2), gap='medium')

conn = st.connection("postgresql", type="sql")
df1 = conn.query('select nuri,fuente,titulo,detalle from novedades order by nuri desc limit 100;', ttl="0"),

st.write(df1[0])

