# Streamly – Netflix Viewing Statistics Dashboard

Streamly is an interactive data application built with Streamlit for exploring
Netflix viewing trends across global and country-level Top 10 data.

The application provides two main experiences: exploring Nordic Top 10 trends
by country and time period, and comparing Netflix movies and series side by
side using global viewing statistics, rankings, genres and metadata.

## Features

### Nordic Spotlights

Explore Netflix Top 10 performance across Nordic markets using interactive
filters for:

- Country
- Year
- Month

The selected data is aggregated into Top 10 charts based on title popularity.

### Compare Movies and Series

Compare two Netflix titles side by side using global viewing statistics.

The comparison includes:

- Weeks in Global Top 10
- Best Global Rank
- Average Global Rank
- Weekly Views
- Genre information
- Title metadata

When two titles are selected, their viewing performance can also be compared
over time.

## Data

The application uses four prepared datasets:

| Dataset | Purpose |
| --- | --- |
| `FactGlobal_Final.csv` | Global weekly viewing statistics and rankings |
| `FactCountry_Final.csv` | Country-level Top 10 data |
| `DimMetaData_Final.csv` | Title metadata |
| `DimGenre_Final.csv` | Genre information |

The structure separates analytical facts from descriptive title data, making
the datasets easier to reuse across different parts of the application.

## Application Architecture

The project follows a modular structure instead of keeping the entire
Streamlit application in a single script.

```text
src/netflix/
├── app.py
├── assets/
│   ├── data/
│   ├── image/
│   └── style/
├── components/
│   ├── branding.py
│   ├── charts.py
│   ├── filters.py
│   ├── footer.py
│   ├── metrics.py
│   └── title_card.py
├── pages/
│   ├── home.py
│   └── compare.py
└── utils/
    ├── constants.py
    ├── data.py
    ├── helpers.py
    └── theme.py
```

### Pages

`home.py` handles the Nordic Top 10 dashboard and its country, year and month
filters.

`compare.py` handles title comparison, KPI metrics, metadata and viewing
performance.

### Components

Reusable Streamlit UI functionality is separated into components for:

- Charts
- Filters
- Branding
- Metrics
- Title cards
- Footer content

### Data Layer

`utils/data.py` provides reusable functions for loading, filtering and
preparing the datasets.

Streamlit's `@st.cache_data` is used when loading the CSV files to avoid
unnecessary repeated reads during application reruns.

## Example Data Processing

Country-level data is filtered based on the user's selected country, year and
month before being passed to the visualization layer.

For Top 10 charts, titles are grouped by title and category and their
popularity scores are aggregated before selecting the ten highest-performing
titles.

Global title statistics are calculated from weekly observations, including:

- Cumulative weeks in the Top 10
- Best weekly rank
- Average weekly rank
- Weekly views over time

## Tech Stack

- Python
- Streamlit
- Pandas
- HTML/CSS
- Git / GitHub

## Running the Application

### 1. Clone the repository

```bash
git clone https://github.com/mandcoder/Streamlit_NF.git
cd Streamlit_NF
```

### 2. Install dependencies

Using `uv`:

```bash
uv sync
```

### 3. Run Streamly

```bash
uv run streamlit run src/netflix/app.py
```

The Streamlit application will then be available through the local URL
provided by Streamlit.

## Project Highlights

This project demonstrates how prepared analytical datasets can be transformed
into an interactive data product.

The implementation focuses on separating responsibilities between data
loading, data preparation, reusable UI components and application pages,
rather than building the entire dashboard in a single Streamlit script.

The result is a more maintainable application where individual components,
visualizations and data functions can be developed independently.
