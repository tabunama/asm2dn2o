import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

project = "ASM2d-GHG/N₂O"
author = "Taher Abunama"
copyright = "2026"
release = "0.1.1"

extensions = [
    "myst_parser",
    "sphinx_rtd_theme",
]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_title = "ASM2d-GHG/N₂O"
html_short_title = "ASM2d-GHG/N₂O"
html_static_path = ["_static"]