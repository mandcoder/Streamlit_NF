# ---------------------------------------------------------
# home.py
# Purpose: Homepage with nordic Top Charts
# ---------------------------------------------------------

from netflix.components.filters import render_filters
from netflix.components.footer import disclaimer_footer
from netflix.components.charts import render_top_charts
from netflix.components.branding import render_logo, render_header
from netflix.utils.constants import STYLES_PATH
from netflix.utils.helpers import read_css
from netflix.utils.data import get_country_df

read_css(STYLES_PATH / "main.css")
read_css(STYLES_PATH / "home.css")


# Logotype
render_logo()

# Data
df = get_country_df()

# Header
render_header()

# Filter
selected_country, selected_year, selected_month = render_filters(df)

# Filtering
filtered_df = df[
    (df["country_name"] == selected_country)
    & (df["year"] == selected_year)
    & (df["month_name"] == selected_month)
]

# Chart
render_top_charts(filtered_df)

# Footer
disclaimer_footer()
