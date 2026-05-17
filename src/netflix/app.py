# -----------------------------------
# app.py
# Purpose: Starting point for the App
# -----------------------------------

import streamlit as st

st.set_page_config(
    page_title="Streamly Film Statistics",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)

pages = [
    st.Page("pages/home.py", title="Nordic spotlights"),
    st.Page("pages/compare.py", title="Compare Movies and Series"),
]

pg = st.navigation(pages)
pg.run()
