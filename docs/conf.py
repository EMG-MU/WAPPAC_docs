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

# html_theme = "sphinx_book_theme"
# html_theme_options = {
#     "repository_url": "https://github.com/EMG-MU/WAPPAC_docs",  # replace
#     "use_repository_button": True,
#     "use_download_button": True,
#     "use_fullscreen_button": True,
#     "show_toc_level": 2,
# }

# html_theme = "pydata_sphinx_theme"
# html_theme_options = {
#     "show_nav_level": 2,
#     "navbar_start": ["navbar-logo"],
#     "navbar_end": ["search-field.html", "navbar-icon-links"],
# }

# -- Theme Options for Piccolo ---
html_theme = "piccolo_theme"

# (Optional) Piccolo theme options
html_theme_options = {
    # The default theme is 'light'. Other options are 'dark' and 'auto'.
    "default_theme": "auto",

    # Show the symbol for the current page in the sidebar.
    "show_current_page_in_sidebar": True,

    # Show the table of contents in the right sidebar.
    # The levels of headings to show are controlled by the `show_toc_level`
    # option of the `toc` directive in your reST files.
    "show_right_sidebar": True,

    # The depth of the table of contents in the right sidebar.
    "right_sidebar_toc_depth": 2,

    # An absolute URL to your project's source code, e.g. on GitHub.
    "source_url": "https://github.com/your-username/your-repo/",

    # The text to display for the source link.
    "source_display_text": "View on GitHub",

    # An icon to show for the source link.
    # The value should be a path to an SVG file in your _static folder.
    # "source_icon": "_static/github.svg",

    # (Optional) Add a banner to the top of the page.
    # "banner_text": "This is a pre-release version of the documentation.",
    # "banner_icon": "⚠️", # You can use any emoji or text
}

# -- Theme Options for Shibuya ---
# html_theme = "shibuya"
# html_theme_options = {
#     # The URL to your GitHub repository. This is different from sphinx_book_theme's "repository_url".
#     "github_url": "https://github.com/EMG-MU/WAPPAC_docs",
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
