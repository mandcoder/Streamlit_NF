# -------------------------------------------
# footer.py
# Purpose: Reusable disclaimer for all pages
# -------------------------------------------

import streamlit as st


DISCLAIMER_TEXT = (
    "This application is a student project created for educational purposes only.",
    "Netflix Top 10 data is sourced from Tudum by Netflix.",
    "Movie titles, images, trailers, trademarks, and related content are the property of their respective owners, including Netflix and IMDb.",
    "We do not claim ownership of any external media or trademarks used in this project.",
    "External links redirect users to third-party websites.",
)


def disclaimer_footer() -> None:
    """Render the disclaimer footer."""
    disclaimer_items = "".join(
        f'<p class="disclaimer-text">{line}</p>' for line in DISCLAIMER_TEXT
    )

    st.markdown(
        f"""
        <footer class="disclaimer-footer" aria-label="Educational and legal disclaimer">
            <div class="disclaimer-title">Disclaimer</div>
            {disclaimer_items}
        </footer>
        """,
        unsafe_allow_html=True,
    )
