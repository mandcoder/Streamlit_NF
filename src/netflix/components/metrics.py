# ----------------------------------------------
# metrics.py
# Purpose: Reusable KPI metric card components
# ----------------------------------------------
# show_kpi_card is the atomic building block — renders a single KPI card in a given column.
# show_kpi is a convenience wrapper that creates columns and loops show_kpi_card.
# Use show_kpi_card when you need full control over the layout.
# Use show_kpi when you just want a row of KPI cards.
# ---------------------------------------------

from typing import Any
import streamlit as st
from streamlit.delta_generator import DeltaGenerator


def show_kpi_card(col: DeltaGenerator, label: str, value: Any) -> None:
    """
    Renders a single KPI metric card.
    """
    col.metric(label, value, border=True)


def show_kpi(metrics: list[tuple[str, Any]]) -> None:
    """
    Renders a row of KPI cards.
    Takes a list of (label, value) tuples.
    """
    if not metrics:
        st.warning("Data is missing")
        return

    cols = st.columns(len(metrics))
    for col, (label, value) in zip(cols, metrics):
        show_kpi_card(col, label, value)
