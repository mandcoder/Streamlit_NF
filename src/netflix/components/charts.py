# ----------------------------------------------------
# components/visuals.py
# Purpose: Chart components for home and compare pages
# ----------------------------------------------------

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from netflix.utils.theme import (
    COLOR_MAP,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
    SURFACE,
    BG_PRIMARY,
    BG_SECONDARY,
    AMBER_PRIMARY,
    ORANGE_ACCENT,
)
from netflix.utils.data import build_top_charts_data, format_score


def render_top_charts(df) -> None:
    """
    Renders a horizontal bar chart with the Top 10 titles.
    Color-coded by category.
    """
    top, _ = build_top_charts_data(df)

    if top.empty:
        st.warning("No data available for selected filter.")
        return

    fig = go.Figure()

    # Draw one trace per category to display a legend
    for category, color in COLOR_MAP.items():
        subset = top[top["category"] == category]
        if subset.empty:
            continue

        fig.add_trace(
            go.Bar(
                y=subset["show_title"].str.title(),
                x=subset["total_score"],
                orientation="h",
                name="Movies" if category == "Movie" else "Series",
                marker_color=color,
                text=subset["total_score"].apply(format_score),
                textposition="outside",
                textfont=dict(color=color, size=12),
            )
        )

    fig.update_layout(
        title=dict(
            text='<b style="font-size:18px; color:{TEXT_PRIMARY};">Top Charts</b><br><br><span style="font-weight: 100; font-family: sans-serif;">This chart shows overall popularity by combining weekly rankings into a single score. Higher-ranked titles earn more points each week, and these points are summed over time,<br> so titles that stay popular longer achieve higher scores.<br><br><br></span>',
            font=dict(color=TEXT_PRIMARY, size=11),
        ),
        paper_bgcolor=BG_SECONDARY,
        plot_bgcolor=BG_SECONDARY,
        bargap=0.35,
        font=dict(color=TEXT_SECONDARY),
        xaxis=go.layout.XAxis(
            showgrid=True,
            gridwidth=1,
            gridcolor="rgba(158, 150, 137, 0.3)",
            showticklabels=True,
            zeroline=False,
            tickfont=dict(color=TEXT_PRIMARY, size=11),
        ),
        yaxis=go.layout.YAxis(
            showgrid=False,
            tickfont=go.layout.yaxis.Tickfont(size=11, color=TEXT_PRIMARY),
            categoryorder="array",
            categoryarray=top["show_title"].str.title().to_list(),
        ),
        legend=go.layout.Legend(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor=BG_SECONDARY,
            font=dict(color=TEXT_PRIMARY, size=12),
        ),
        margin=go.layout.Margin(l=20, r=60, t=110, b=20),
    )
    st.plotly_chart(fig, use_container_width=True)


def show_views_chart(stats_left, stats_right, title_left, title_right):
    """
    Renders a line chart comparing weekly views for two titles over time.
    """
    stats_left["chart_data"]["week"] = pd.to_datetime(stats_left["chart_data"]["week"])
    stats_right["chart_data"]["week"] = pd.to_datetime(
        stats_right["chart_data"]["week"]
    )

    x_min = max(
        stats_left["chart_data"]["week"].min(), stats_right["chart_data"]["week"].min()
    )
    x_max = max(
        stats_left["chart_data"]["week"].max(), stats_right["chart_data"]["week"].max()
    )

    fig_views = go.Figure()

    if stats_left is not None:
        fig_views.add_trace(
            go.Scatter(
                x=stats_left["chart_data"]["week"],
                y=stats_left["chart_data"]["weekly_views"],
                name=title_left.title(),
                line=dict(color=AMBER_PRIMARY, width=2),
            ),
        )

    if stats_right is not None:
        fig_views.add_trace(
            go.Scatter(
                x=stats_right["chart_data"]["week"],
                y=stats_right["chart_data"]["weekly_views"],
                name=title_right.title(),
                line=dict(color=ORANGE_ACCENT, width=2),
            )
        )

    fig_views.update_layout(
        title=dict(
            text="Views over time",
            font=dict(color=TEXT_PRIMARY, size=16),
        ),
        paper_bgcolor=BG_PRIMARY,
        plot_bgcolor=BG_SECONDARY,
        hovermode=False,
        xaxis=go.layout.XAxis(
            showgrid=True,
            gridwidth=1,
            gridcolor="rgba(158, 150, 137, 0.3)",
            showticklabels=True,
            zeroline=False,
            range=[x_min.strftime("%Y-%m-%d"), x_max.strftime("%Y-%m-%d")],
            tickfont=dict(color=TEXT_PRIMARY, size=11),
        ),
        yaxis=go.layout.YAxis(
            showgrid=False,
            showticklabels=True,
            zeroline=False,
            tickfont=dict(color=TEXT_PRIMARY, size=11),
        ),
        legend=go.layout.Legend(
            bgcolor=SURFACE,
            font=dict(color=TEXT_PRIMARY),
            itemsizing="constant",
        ),
    )
    st.plotly_chart(fig_views, use_container_width=True)
