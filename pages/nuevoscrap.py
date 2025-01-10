import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from langchain.llms import LlamaLLM
from langchain.chains import LLChain
from langchain.prompts import ChatPromptTemplate

MODEL_NAME = "llama3.2"

def parse_with_olama(dom_chunks, parse_description):
    llama = LlamaLLM(model_name=MODEL_NAME) if MODEL_NAME else None
    prompts = [
        ChatPromptTemplate("Extract the following information from the text: {parse_description}", dom_content=chunk)
        for chunk in dom_chunks
    ]
    chain = LLChain.from_prompt(prompts)
    return chain.run_chain()

def scrape_website(url):
    chrome_options = Options()
    chrome_driver_path = "./chromedriver"  # Update this path based on your OS
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)
    page_source = driver.page_source
    driver.quit()

    return page_source

def extract_body_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    body_content = soup.body
    return str(body_content) if body_content else ""

def clean_content(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')
    for tag in soup(['script', 'style']):
        tag.decompose()
    cleaned_text = soup.get_text("\n", strip=True)
    return cleaned_text

st.title("AI Web Scraper")
url = st.text_input("Enter a website URL")

if st.button("Scrape Site"):
    st.write("Scraping the website...")
    # Further logic will go here

if st.button("Scrape Site"):
    raw_html = scrape_website(url)
    body_content = extract_body_content(raw_html)
    cleaned_content = clean_content(body_content)
    
    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)

    parse_description = st.text_area("Describe what you want to parse:")

    if st.button("Parse Content"):
        dom_chunks = [cleaned_content[i:i+6000] for i in range(0, len(cleaned_content), 6000)]
        result = parse_with_olama(dom_chunks, parse_description)
        st.write(result)
