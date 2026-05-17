# ------------------------------------------------------------
# helpers.py
# Purpose: Helper functions for CSS injection and file reading
# ------------------------------------------------------------

import streamlit as st


def read_textfile(path):
    """Reads a text file and returns its content."""
    with open(path) as file:
        return file.read()


def read_css(path):
    """Reads a CSS file and injects it into Streamlit."""
    css = read_textfile(path)
    st.write(
        f"<style>{css}</style>",  # wraps the CSS inside an HTML style tag
        unsafe_allow_html=True,  # required because Streamlit blocks HTML by default
    )
