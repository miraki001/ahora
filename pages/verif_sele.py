import streamlit as st
import pandas as pd
from time import sleep
from bs4 import BeautifulSoup
import undetected_chromedriver as uc

import requests
import shutil
import os

if __name__ == "__main__":

    # instantiate a Chrome browser
    driver = uc.Chrome(
        use_subprocess=False,
    )

    # visit the target URL
    driver.get("https://www.euromonitor.com/insights/drinks")

    html_content = driver.page_source

    soup=BeautifulSoup(html_content, "html.parser")
    driver.quit()
