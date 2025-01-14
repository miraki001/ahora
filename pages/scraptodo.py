import streamlit as st
import os
import sys
import psutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from os.path import exists
import csv
from time import sleep
import pandas as pd
import re
from streamlit_extras.image_in_tables import table_with_images
import streamlit.components.v1 as components
from streamlit_echarts import st_echarts
import base64
import psycopg2
from sqlalchemy import text

my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"


def scrap()



conn = st.connection("postgresql", type="sql")
qq = "select * from fuentes_py where proyecto_nuri = 1 and activa = 'S'  ;"
df1 = conn.query(qq, ttl="0"),
df = df1[0]
st.write(df)
st.write(len(df))



for i in range(len(df)):
  vsepa = df['separador'][i])
  vtitu = df['xpath_titulo'][i])
  vdeta = df['xpath_detalle'][i])
  vlink = df['xpath_link'][i])
  vimag = df['xpath_image'][i])
  vnuri = df['nuri'][i]
  vfuente = df['descrip'][i]
  vurl = df['fuente'][i]
  st.write(df['nuri'][i])
