import streamlit as st
import pandas as pd
import numpy as np
import itables.options as it_op
from itables.streamlit import interactive_table

#default=["copyHtml5", "csvHtml5", "excelHtml5", "colvis"],
default=["copyHtml5", "csvHtml5", "excelHtml5"],

it_args = {}
it_args["buttons"] = default
it_args["select"] = True

  




conn = st.connection("postgresql", type="sql")
df1 = conn.query('select nuri,fuente,fecha,titulo,detalle from novedades order by nuri desc limit 100;', ttl="0"),

st.write(df1[0])

interactive_table(df1[0],
                  caption='Countries',
                  select=True,
                  selected_rows=[0, 1, 2, 99, 99],
                  buttons=['copyHtml5', 'csvHtml5', 'excelHtml5', 'colvis'])

t = interactive_table(df1[0], **it_args )

df1 = df1[pd.notnull(df['titulo'])]





