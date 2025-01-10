import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
MODEL_NAME = "llama3"
model = OllamaLLM(model="llama3")
my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"

def parseUsingOllama (domChunks , parseDescription) :
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    finalResult = []
    for counter , chunk in enumerate (domChunks , start=1) :
        result = chain.invoke(
                                {"dom_content": chunk , "parseDescription": parseDescription}
                              )
        print(f"Parsed Batch {counter} of {len(domChunks)}")
        finalResult.append(result)
    return "\n".join(finalResult)


def parse_with_olama(dom_chunks, parse_description):
    llama = LlamaLLM(model_name=MODEL_NAME) if MODEL_NAME else None
    prompts = [
        ChatPromptTemplate("Extract the following information from the text: {parse_description}", dom_content=chunk)
        for chunk in dom_chunks
    ]
    chain = LLChain.from_prompt(prompts)
    return chain.run_chain()

def scrape_website(url):
    options = webdriver.ChromeOptions()
    
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    #options.add_argument(f"--window-size={width}x{height}")
    options.add_argument(f"--user-agent={my_user_agent}")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-features=NetworkService")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-features=VizDisplayCompositor")
    
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)

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
    raw_html = scrape_website(url)
    body_content = extract_body_content(raw_html)
    cleaned_content = clean_content(body_content)
    
    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)

    parse_description = st.text_area("Describe what you want to parse:")

    if st.button("Parse Content"):
        dom_chunks = [cleaned_content[i:i+6000] for i in range(0, len(cleaned_content), 6000)]
        st.write('aca')
        result = parseUsingOllama(dom_chunks, parse_description)
        st.write(result)
