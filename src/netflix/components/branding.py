# -------------------------------------
# branding.py
# Purpose: Reusable branding components
# -------------------------------------

import streamlit as st
from netflix.utils.constants import IMAGE_PATH
from netflix.utils.theme import TEXT_SECONDARY, AMBER_PRIMARY


def render_logo() -> None:
    """
    Renders the Streamly logo and a divider.
    """
    st.image(str(IMAGE_PATH / "Logga_Streamly.png"), width=200)


def render_header() -> None:
    """Renders the Nordic Spotlight header and description."""

    st.markdown(
        f"<p style=' color: {AMBER_PRIMARY}; font-weight: 400; letter-spacing: 0.1em; margin-bottom: 0; margin-top: 2rem;'>NORDIC SPOTLIGHT</p>",
        unsafe_allow_html=True,
    )
    st.title("What the Nordics are watching")
    st.markdown(
        f"<p style='color: {TEXT_SECONDARY};'>Discover the Top 10 films and series in the Nordics. <br>"
        "Filter by country, year and month to dive deeper.<br><br></p>",
        unsafe_allow_html=True,
    )


def render_compare_header() -> None:
    """
    Renders the compare page header and description.
    """
    st.title("Compare Movies/Series")
    st.markdown(
        f"<p style='color: {TEXT_SECONDARY};'>Find out more about your favourite movies and shows, or find something new to watch.<br> "
        "Search for a show below and add another to compare it to.<br><br></p>",
        unsafe_allow_html=True,
    )
