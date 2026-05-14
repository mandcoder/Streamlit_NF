# ---------------------------------------------------------
# helpers.py
# Purpose: Helper functions for reading files, loading data,
# and preparing chart data
# ------------------------------------------------------------------------------------------------------------

from netflix.utils.constants import DATA_PATH  # path to the data-folder
import pandas as pd
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


@st.cache_data
def get_global_df():
    """Loads normalized global data."""
    return pd.read_csv(DATA_PATH / "FactGlobal_Final.csv")


@st.cache_data
def get_metadata_df():
    """Loads metadata with posters, trailers, and descriptions."""
    return pd.read_csv(DATA_PATH / "DimMetaData_Final.csv")


@st.cache_data
def get_country_df():
    """Loads normalized country data."""
    return pd.read_csv(DATA_PATH / "FactCountry_Final.csv")


def build_top_charts_data(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Calculates popularity_score per title and category.
    Returns the top 10 titles sorted by score
    in ascending order for a horizontal bar chart.
    """

    grouped = (
        df.groupby(["show_title", "category"])["popularity_score"].sum().reset_index()
    )

    grouped.columns = ["show_title", "category", "total_score"]

    # selects the most popular titles and places the highest score at the top of the bar chart
    top_10 = (
        grouped.sort_values("total_score", ascending=False)
        .head(10)
        .sort_values("total_score", ascending=True)
    )
    return top_10, grouped
