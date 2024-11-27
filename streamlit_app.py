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
if select:
    it_args["select"] = True
    it_args["selected_rows"] = [0, 1, 2, 100, 207]
if classes != it_opt.classes.split(" "):
    it_args["classes"] = classes
if style != it_opt.style:
    it_args["style"] = style

if buttons:
    it_args["buttons"] = buttons


if caption:
    it_args = {"caption": caption, **it_args}



conn = st.connection("postgresql", type="sql")
df1 = conn.query('select nuri,fuente,titulo,detalle from novedades order by nuri desc limit 100;', ttl="0"),
with col1[0]:
  st.write(df1[0])

  t = interactive_table(df1[0], **it_args )

  st.header("Table state")
  st.markdown(
      """The value returned by `interactive_table` is
  a dict that contains the index of the selected rows:"""
  )
  st.write(t)

