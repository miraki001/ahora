import streamlit as st
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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
