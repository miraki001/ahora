import streamlit as st
import pandas as pd
import numpy as np
import itables.options as it_op
from itables.streamlit import interactive_table

buttons = st.sidebar.multiselect(
    "Buttons",
    options=["pageLength", "copyHtml5", "csvHtml5", "excelHtml5", "colvis"],
    default=["copyHtml5", "csvHtml5", "excelHtml5", "colvis"],
)


it_args = {}
it_args["buttons"] = buttons






conn = st.connection("postgresql", type="sql")
df1 = conn.query('select nuri,fuente,titulo,detalle from novedades order by nuri desc limit 100;', ttl="0"),

st.write(df1[0])

t = interactive_table(df1[0], **it_args )

st.header("Table state")
st.markdown(
    """The value returned by `interactive_table` is
  a dict that contains the index of the selected rows:"""
)
st.write(t)

