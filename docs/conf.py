# docs/conf.py -- minimal Sphinx configuration for MyST + sphinx-book-theme
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = "My Wave Energy Project"
author = "Your Name"
release = "0.1"

extensions = [
    "myst_parser",
    "sphinxcontrib.bibtex",
    "sphinx.ext.mathjax",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_static_path = ["_static"]

html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": "https://github.com/YOURUSER/YOURREPO",  # replace
    "use_repository_button": True,
    "use_download_button": True,
    "use_fullscreen_button": True,
    "show_toc_level": 2,
}

# MyST (Markdown) settings
myst_enable_extensions = [
    "amsmath",
    "dollarmath",
    "deflist",
    "html_admonition",
    "html_image",
]
myst_heading_anchors = 3

# BibTeX
bibtex_bibfiles = ["refs.bib"]

# If you want logo/favicon, add:
# html_logo = "_static/logo.png"
# html_favicon = "_static/favicon.ico"
