import streamlit as st

st.title("Mercury Prize Winners")

def get_table():
    url = "https://en.wikipedia.org/wiki/Mercury_Prize"
    xpath = "//table[contains(@class, 'wikitable')]"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # we need this since we'll run the container as root
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    # wait for the table to load
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )

    element_html = element.get_attribute("outerHTML")

    # remove links
    soup = BeautifulSoup(element_html, "html.parser")


if st.button("Load from Wikipedia"):
    content = get_table()
    st.html(content)
