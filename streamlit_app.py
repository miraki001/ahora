import streamlit as st
import pandas as pd
import numpy as np

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)



conn = st.connection("postgresql", type="sql")
df1 = conn.query('select nuri,fuente,titulo,detalle from novedades order by nuri desc limit 100;', ttl="0"),

event = st.dataframe(
    df1,
    key="data",
    on_select="rerun",
    selection_mode=["multi-row", "multi-column"],
)

event.selection
