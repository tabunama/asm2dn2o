import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

project = "asm2dn2o"
author = "Taher Abunama"
release = "0.1.0"

extensions = [
    "myst_parser",
    "sphinx_rtd_theme",
]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]