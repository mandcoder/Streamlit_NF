# ---------------------------------------------------------
# data.py
# Purpose: Data loading and preparation functions
# ---------------------------------------------------------
from typing import Any
import pandas as pd
import streamlit as st

from netflix.utils.constants import DATA_PATH


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


@st.cache_data
def get_genre_df():
    """Fetches genre data for all titles."""
    return pd.read_csv(DATA_PATH / "DimGenre_Final.csv")


def get_genres(df_genre: pd.DataFrame, title: str) -> str:
    """
    Returns genres for a title as a comma-separated string.
    """
    genres = df_genre[df_genre["show_title"] == title.lower()]["genre"].to_list()
    return ", ".join(genres) if genres else "Data is not available"


def get_stats(df_global: pd.DataFrame, title: str) -> dict | None:
    """
    Fetches global stats for a given title.
    Returns dict or None.
    """
    data = df_global[df_global["show_title"] == title]
    if data.empty:
        return None
    return {
        "global_weeks_in_top10": int(data["cumulative_weeks_in_top_10"].max()),
        "global_best_rank": int(data["weekly_rank"].min()),
        "global_avg_rank": round(data["weekly_rank"].mean()),
        "chart_data": data[["week", "weekly_views", "weekly_rank"]].sort_values("week"),
    }


def get_metadata(df_metadata: pd.DataFrame, title: str):
    """
    Fetches metadata for a given title.
    Returns row or None.
    """
    match = df_metadata[df_metadata["show_title"] == title.lower()]
    return match.iloc[0] if not match.empty else None


def format_score(v: float) -> str:
    """Formats score, shows K for thousands, otherwise integer."""
    if v >= 1000:
        return f"{int(v / 1000)}K"
    return str(int(v))


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


def extract_metrics_data(
    stats: dict | None, keys: list[tuple[str, str]]
) -> list[tuple[str, Any]] | None:
    """
    Builds a list of KPI metrics from a stats dict.
    Takes a list of (label, key) tuples.
    """
    if not stats:
        return None
    return [(label, stats[key]) for label, key in keys]


def get_title_data(
    title: str | None,
) -> tuple[str | None, dict | None, pd.Series | None]:
    """Fetches genres, stats and metadata for a given title. Returns None if no title."""
    if not title:
        return None, None, None
    return (
        get_genres(get_genre_df(), title),
        get_stats(get_global_df(), title),
        get_metadata(get_metadata_df(), title),
    )
