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
df1 = conn.query('select nuri,fuente,titulo,detalle from novedades order by nuri desc limit 100;', ttl="0"),

st.write(df1[0])

show(df1[0], search={"regex": True, "caseInsensitive": True, "search": "s.ain"})

t = interactive_table(df1[0], **it_args )





