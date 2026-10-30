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
      .stApp {background: #0b0b0c;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      iframe {border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

APP_DIR = Path(__file__).resolve().parent
PREFERRED_NAME = "card_generator.html"


def find_html_file() -> Path | None:
    """Find the card HTML even if it was renamed or placed in a subfolder."""
    # 1. Exact expected name next to app.py
    exact = APP_DIR / PREFERRED_NAME
    if exact.is_file():
        return exact

    # 2. Same name with different capitalisation, anywhere in the repo
    for path in APP_DIR.rglob("*.html"):
        if path.name.lower() == PREFERRED_NAME:
            return path

    # 3. Any HTML file whose name looks like the card generator
    #    (e.g. "card_generator (1).html", "card_generator__2_.html")
    candidates = sorted(
        p for p in APP_DIR.rglob("*.html")
        if "card" in p.name.lower() and ".git" not in p.parts
    )
    if candidates:
        return candidates[0]

    # 4. Fall back to the only HTML file in the repo, if there is exactly one
    all_html = [p for p in APP_DIR.rglob("*.html") if ".git" not in p.parts]
    if len(all_html) == 1:
        return all_html[0]

    return None


html_file = find_html_file()

if html_file is None:
    st.error(
        f"Couldn't find **{PREFERRED_NAME}**. Upload it to your GitHub repo in the "
        "same folder as `app.py`, then reboot the app."
    )
    files = sorted(
        str(p.relative_to(APP_DIR))
        for p in APP_DIR.rglob("*")
        if p.is_file() and ".git" not in p.parts
    )
    st.write("Files the app can currently see:")
    st.code("\n".join(files) or "(none)")
    st.stop()

html = html_file.read_text(encoding="utf-8")

# Height is generous so the full layout fits; scrolling handles small screens
components.html(html, height=1500, scrolling=True)
