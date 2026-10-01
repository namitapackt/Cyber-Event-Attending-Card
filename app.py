from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Packt | I'm Attending Card Generator",
    page_icon="🎟️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Strip Streamlit's default chrome/padding so the page looks like the standalone HTML
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      [data-testid="stToolbar"], [data-testid="stDecoration"] {display: none;}
      .stApp {background: #050816;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      iframe {border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

HTML_FILE = Path(__file__).parent / "card_generator.html"
html = HTML_FILE.read_text(encoding="utf-8")

# Height is generous so the full layout fits; scrolling handles small screens
components.html(html, height=1500, scrolling=True)
