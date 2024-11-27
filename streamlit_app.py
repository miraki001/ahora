import streamlit as st
import pandas as pd
import numpy as np
import itables.options as it_op
from itables.streamlit import interactive_table



it_args = {}
it_args["buttons"] = buttons
it_args["select"] = True






conn = st.connection("postgresql", type="sql")
df1 = conn.query('select nuri,fuente,titulo,detalle from novedades order by nuri desc limit 100;', ttl="0"),

st.write(df1[0])

t = interactive_table(df1[0], **it_args )





