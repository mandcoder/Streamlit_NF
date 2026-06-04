# ---------------------------------------------------
# filters.py
# Purpose: Reusable filter components
# ---------------------------------------------------

import streamlit as st
import pandas as pd
from streamlit.delta_generator import DeltaGenerator

# Only Nordic countries are shown in the home filter
NORDIC_COUNTRIES = ["Denmark", "Finland", "Iceland", "Norway", "Sweden"]


def render_filters(df: pd.DataFrame) -> tuple[str, int, str]:
    """
    Renders country, year and month dropdowns.
    Returns selected country, year and month.
    """
    available_years = sorted(df["year"].unique(), reverse=True)

    st.markdown(
        "<p style='color: #9E9689; font-weight: 600; letter-spacing: 0.1em; font-size: 0.85rem;'>FILTER</p>",
        unsafe_allow_html=True,
    )
    col_country, col_year, col_month, _, _ = st.columns([1, 1, 1, 2, 2], gap="small")

    with col_country:
        selected_country = st.selectbox(
            label="Country",
            options=NORDIC_COUNTRIES,
            index=NORDIC_COUNTRIES.index("Sweden"),
        )

    with col_year:
        selected_year = st.selectbox(
            label="Year",
            options=available_years,
            index=0,  # latest year
        )

    with col_month:  # Filters months available for selected year
        month_available = (
            df[df["year"] == selected_year][["month", "month_name"]]
            .drop_duplicates()
            .sort_values("month", ascending=False)["month_name"]
            .tolist()
        )
        selected_month = st.selectbox(
            label="Month",
            options=month_available,
            index=0,  # latest month
        )

    return selected_country, selected_year, selected_month


def compare_filters(
    df: pd.DataFrame,
) -> tuple[DeltaGenerator, DeltaGenerator, str | None, str | None]:
    """
    Renders two title dropdowns for the compare page.
    Returns left column, right column, and selected titles.
    """
    all_titles = sorted(df["show_title"].unique())
    left_box, right_box = st.columns(2, gap="large", vertical_alignment="top")

    with left_box:
        title_left = st.selectbox(
            label="Find movies and series",
            options=all_titles,
            index=None,
            placeholder="Choose a title",
            key="left",
        )

    with right_box:
        title_right = st.selectbox(
            label="Find movies and series",
            options=all_titles,
            index=None,
            placeholder="Choose a title",
            key="right",
        )

    return left_box, right_box, title_left, title_right
