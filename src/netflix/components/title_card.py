# ----------------------------------------------------
# cards.py
# Purpose: Reusable card components for title display
# ----------------------------------------------------

import streamlit as st
import pandas as pd
from typing import Any
from streamlit.delta_generator import DeltaGenerator
from netflix.components.metrics import show_kpi
from netflix.utils.theme import TEXT_SECONDARY, AMBER_PRIMARY


def show_poster(meta: pd.Series | None) -> None:
    """
    Renders the title poster.
    Shows placeholder if image is unavailable.
    """
    if meta is not None and str(meta["image"]) != "nan":
        st.markdown(
            f'<img src="{meta["image"]}" style="height:350px; width:250px; object-fit:cover; border-radius:4px;">',
            unsafe_allow_html=True,
        )
    else:
        st.caption("Image is not available")


def show_info(title: str, genres: str, rating: str) -> None:
    """Renders title, genre and rating."""
    st.subheader(title.title())
    st.markdown(
        f"<p style='color: {TEXT_SECONDARY}; font-size: 1rem;'>{genres}</p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<p style='color: {AMBER_PRIMARY}; font-size: 1.2rem; font-weight: 600;'>⭐{rating} / 10</p>",
        unsafe_allow_html=True,
    )


def show_trailer_button(trailer_url: str | None) -> None:
    """
    Renders a trailer button if URL is available.
    """
    if trailer_url and trailer_url != "nan":
        st.link_button("▶ Play Trailer", trailer_url)


def show_title_card(
    col: DeltaGenerator,
    title: str,
    meta: pd.Series | None,
    metrics: list[tuple[str, Any]] | None,
    genres: str,
) -> None:
    """Renders a complete title card with poster, info and KPIs."""

    with col:

        st.markdown(
            f"<p style='color: {AMBER_PRIMARY}; font-weight: 700; letter-spacing: 0.1em; font-size: 0.85rem;'>YOUR SELECTION</p>",
            unsafe_allow_html=True,
        )

        col_poster, col_info = st.columns([1, 2], gap="medium")

        with col_poster:
            show_poster(meta)

        with col_info:
            rating = str(meta["rating"]) if meta is not None else "N/A"
            trailer = str(meta["trailer"]) if meta is not None else None

            show_info(title, genres, rating)
            show_trailer_button(trailer)

        st.markdown("<br>", unsafe_allow_html=True)

        if metrics is not None:
            show_kpi(metrics)


def render_card_if_selected(
    box: DeltaGenerator,
    title: str | None,
    meta: pd.Series | None,
    metrics: list[tuple[str, Any]] | None,
    genres: str | None,
    key: str,
) -> None:
    """Renders a title card if a title is selected."""
    if title:
        with box.container(key=key):
            show_title_card(st.container(), title, meta, metrics, genres)
