# --------------------------------------------------------------------
# constants.py
# Purpose: Defines all paths used in the project
# Single responsibility, this file does one thing: handles paths.
#
# Base path
# Path(__file__) = absolute path to this file (constants.py)
# .parents[0]   = utils/          (one level up)
# .parents[1]   = src/netflix/    BASE_PATH (two levels up)
#
# Assets, all static content is stored under assets/
# --------------------------------------------------------------------

from pathlib import Path


BASE_PATH = Path(__file__).parents[1]

ASSETS_PATH = BASE_PATH / "assets"

# Subfolders
IMAGE_PATH = ASSETS_PATH / "image"  # logos and images
STYLES_PATH = ASSETS_PATH / "style"  # CSS files
MARKDOWN_PATH = ASSETS_PATH / "markdown"  # markdown text files
DATA_PATH = ASSETS_PATH / "data"  # CSV files

# Components
COMPONENTS_PATH = BASE_PATH / "components"
