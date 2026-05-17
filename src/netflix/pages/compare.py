# --------------------------------------------------
# pages/compare.py
# Purpose: Compare two Netflix titles side by side
# --------------------------------------------------


from netflix.components.branding import render_logo, render_compare_header
from netflix.components.title_card import render_card_if_selected
from netflix.components.filters import compare_filters
from netflix.components.footer import disclaimer_footer
from netflix.components.charts import show_views_chart
from netflix.utils.constants import STYLES_PATH
from netflix.utils.helpers import read_css
from netflix.utils.data import (
    get_global_df,
    get_metadata_df,
    get_genre_df,
    extract_metrics_data,
    get_title_data,
)

# Read css-files
read_css(STYLES_PATH / "main.css")
read_css(STYLES_PATH / "compare.css")

# KPI metrics definition
TITLE_METRICS = [
    ("Weeks in Top 10", "global_weeks_in_top10"),
    ("Best Global Rank", "global_best_rank"),
    ("Average Global Rank", "global_avg_rank"),
]

# Logotype
render_logo()

# Data
df_global = get_global_df()
df_metadata = get_metadata_df()
df_genre = get_genre_df()

# Page header and description
render_compare_header()

# Filter
left_box, right_box, title_left, title_right = compare_filters(df_global)

# Title cards
genres_left, stats_left, meta_left = get_title_data(title_left)
genres_right, stats_right, meta_right = get_title_data(title_right)

metrics_left = extract_metrics_data(stats_left, TITLE_METRICS)
metrics_right = extract_metrics_data(stats_right, TITLE_METRICS)

render_card_if_selected(
    left_box, title_left, meta_left, metrics_left, genres_left, "left-card"
)
render_card_if_selected(
    right_box, title_right, meta_right, metrics_right, genres_right, "right-card"
)

# Views chart
if title_left and title_right:
    show_views_chart(stats_left, stats_right, title_left, title_right)

# Footer
disclaimer_footer()
