# docs/conf.py -- minimal Sphinx configuration for MyST + sphinx-book-theme
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = "WAPPAC Competition"
author = "Eugenio M. Gelos"
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
# html_css_files = ["custom.css"]

# Figure configuration
numfig = True

numfig_format = {
    'figure': 'Figure %s',
    'table': 'Table %s',
    'code-block': 'Listing %s',
    'section': 'Section %s',
}

extensions = [
    "myst_parser",
    "sphinxcontrib.bibtex",
    "sphinx.ext.mathjax",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

myst_enable_extensions = [
    "amsmath",
    "dollarmath",
    "deflist",
    "html_admonition",
    "html_image",
]

mathjax3_config = {
    "TeX": {
        "equationNumbers": {"autoNumber": "all"},
        "tags": "all",
    },
    "chtml": {
        "displayAlign": "center",
        "displayIndent": "0em",
    }
}

myst_heading_anchors = 3

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# BibTeX
bibtex_bibfiles = ["refs.bib"]

# If you want logo/favicon, add:
# html_logo = "_static/logo.png"
# html_favicon = "_static/favicon.ico"

# -- Theme Options for iccolo ---
html_theme = "piccolo_theme"

# (Optional) Piccolo theme options
html_theme_options = {
    # The color mode. Can be "light", "dark", or "auto".
    "color_mode": "auto",

    # An absolute URL to your project's source code, e.g. on GitHub.
    "source_{pto}rl": "https://github.com/your-username/your-repo/",

    # Configuration for the source link icon and text.
    # This replaces 'source_display_text' and 'source_icon'.
    "source_link_icon": "fa-brands fa-square-github",  # A FontAwesome icon

    # Banner configuration remains the same.
    # "banner_text": "This is a pre-release version of the documentation.",
    # "banner_icon": "⚠️",
}

# # -- Theme Options for Shibuya ---
# html_theme = "shibuya"
# html_theme_options = {
#     # The URL to your GitHub repository. This is different from sphinx_book_theme's "repository_{pto}rl".
#     "github_{pto}rl": "https://github.com/EMG-MU/WAPPAC_docs",
#
#     # The name of the repo that will be displayed on the page.
#     "github_repo": "WAPPAC_docs",
#
#     # The author's name, displayed in the footer.
#     "author": "Your Name or Organization",
#
#     # Color palette for light and dark modes. Can be "light", "dark", or "auto".
#     "color_mode": "auto",
#
#     # Add extra links to the navigation bar.
#     "nav_links": [
#         {"title": "Home", "url": "index"},
#         {"title": "Installation", "url": "installation"},
#         {"title": "About", "url": "about"},
#     ],
#     # Add icon links to the navigation bar.
#     "social_links": [
#         {"icon": "github", "url": "https://github.com/EMG-MU/WAPPAC_docs"},
#         # You can add others like:
#         # {"icon": "twitter", "url": "https://twitter.com/your-handle"},
#     ]
# }

# -- Theme Options for sphinx_book_theme ---
# html_theme = "sphinx_book_theme"
# html_theme_options = {
#     "repository_url": "https://github.com/EMG-MU/WAPPAC_docs",  # replace
#     "use_repository_button": True,
#     "use_download_button": True,
#     "use_fullscreen_button": True,
#     "show_toc_level": 2,
# }

# -- Theme Options for pydata_sphinx_theme ---
# html_theme = "pydata_sphinx_theme"
# html_theme_options = {
#     "show_nav_level": 2,
#     "navbar_start": ["navbar-logo"],
#     "navbar_end": ["search-field.html", "navbar-icon-links"],
# }


