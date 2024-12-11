import streamlit as st


st.set_page_config(layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = True

if "app_id" not in st.session_state:
    st.session_state.app_id = None

if "active_app_id" not in st.session_state:
    st.session_state.active_app_id = None

USER = "admin"
PASSWORD = "admin"

positions = ["top", "under", "side"]

def my_sidebar():
    with st.sidebar:
        st.write("Logged in:", st.session_state.logged_in)
        position_mode = st.radio(
            "Navbar position mode",
            positions,
            # index=positions.index(st.session_state.get("position_mode", "top")),
        )
        sticky_nav = st.checkbox(
            "Sticky navbar", value=st.session_state.get("sticky_nav", True)
        )
        st.session_state["position_mode"] = position_mode
        st.session_state["sticky_nav"] = sticky_nav


def my_heading():
    st.title("Streamlit Multi-Page App")
    st.subheader("This is a multi-page app with a native Streamlit navbar.")
    st.markdown("> But only vizualize well with navbar on `top` position")


def login():
    _, col, _ = st.columns([2, 6, 2])
    with col:
        with st.form(key="login_form"):
            user = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Submit")

        with st.expander("Psst! Here's the login info"):
            st.write(f"Username and Password is:")
            st.markdown(f"""
            ```bash
            {USER}
            ```
            """)

    if submitted:
        if user == USER and password == PASSWORD:
            st.session_state.logged_in = True
            st.session_state.app_id = "app_default"
            st.rerun()
        else:
            st.toast("Invalid username or password", icon="❌")


def account():
    st.write("Account page")
    st.caption("This is a protected page. Only logged in users can view this.")


def settings():
    st.button("Theme")


def logout():
    st.session_state.logged_in = False
    st.session_state.app_id = None
    st.session_state.active_app_id = None
    st.rerun()

st.logo(
    image="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.svg",
    icon_image="https://streamlit.io/images/brand/streamlit-mark-color.png"
)

login_page = st.Page(login, title="Log in", icon=":material/login:")
account_page = st.Page(account, title="Account", icon=":material/account_circle:")
settings_page = st.Page(settings, title="Settings", icon=":material/settings:")
dashboard = st.Page("dashboard.py", title="Dashboard", icon=":material/dashboard:", default=True)
bugs = st.Page("reports/bugs.py", title="Bug reports", icon=":material/bug_report:")
alerts = st.Page("reports/alerts.py", title="System alerts", icon=":material/notification_important:")
search = st.Page("tools/search.py", title="Search", icon=":material/search:")
history = st.Page("tools/history.py", title="History", icon=":material/history:")

# Streamlit Navigation
if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [account_page, settings_page, logout],
            "Reports": [dashboard, bugs, alerts],
            "Tools": [search, history],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()
