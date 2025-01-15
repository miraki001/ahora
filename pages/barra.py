
"""
st.set_page_config(page_title='First app', page_icon="📊", initial_sidebar_state="expanded", layout='wide')
from streamlit.components.v1 import html
st.sidebar.text("menu options")
html("""<script>
        var decoration = window.parent.document.querySelectorAll('[data-testid="stDecoration"]')[0];
        var isVisible = true;

        function toggleVisibility() {
            isVisible = !isVisible;
            //decoration.style.display = isVisible ? "flex" : "none";
            decoration.innerText = isVisible ? "Welcome, Streamlit App!" : "";
        }

        // Locate elements
        var sidebar = window.parent.document.querySelectorAll('[data-testid="stSidebar"]')[0];

        // Observe sidebar size
        function outputsize() {
            decoration.style.left = `${sidebar.offsetWidth}px`;
        }

        new ResizeObserver(outputsize).observe(sidebar);

        // Adjust sizes
        outputsize();
        decoration.style.height = "3.0rem";
        decoration.style.right = "45px";

        // Adjust text decorations
        decoration.innerText = "Miraki - Plataforma de Vigilancia Tecnologica e Inteligencia Competitiva";
        decoration.style.fontWeight = "bold";
        decoration.style.display = "flex";
        decoration.style.justifyContent = "center";
        decoration.style.alignItems = "center";

        // Add click event listener
        decoration.addEventListener("click", toggleVisibility);
    </script>
""", width=0, height=0)

"""
