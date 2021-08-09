#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os
from datetime import datetime

AUTHOR = "Julio Melanda"
SITENAME = "Julio Cesar Eiras Melanda"
SITETITLE = "Julio Melanda's Blog"
SITEURL = ""

BASEDIR = os.path.abspath(os.path.dirname(__file__))

PATH = "content"

TIMEZONE = "Europe/Copenhagen"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (("Want to hire me?", "https://jcemelanda.github.io/curriculum/"),)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

THEME = os.path.join(BASEDIR, "Flex")

TYPOGRIFY = True

ROBOTS = "index, follow"

COPYRIGHT_YEAR = datetime.today().year

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

# # Enable i18n plugin.
# PLUGINS = ["i18n_subsites"]
# # Enable Jinja2 i18n extension used to parse translations.
# JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

# Default theme language.
I18N_TEMPLATES_LANG = "en"

PLUGIN_PATHS = [os.path.join("..", "pelican-plugins")]

SITELOGO = SITEURL + "/images/Julio.jpg"

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

DATE_FORMATS = {
    "en": "%m-%d-%Y",
    "pt_BR": "%d-%m-%Y",
}
BROWSER_COLOR = "#666666"
PYGMENTS_STYLE = "github"
PYGMENTS_STYLE_DARK = "vim"


SOCIAL = (
    ("github", "https://github.com/jcemelanda"),
    ("linkedin", "https://www.linkedin.com/in/jcemelanda"),
    ("twitter", "https://twitter.com/jcemelanda"),
)

STATIC_PATHS = ["images", "extra/custom.css"]

EXTRA_PATH_METADATA = {
    "extra/custom.css": {"path": "static/custom.css"},
}

CUSTOM_CSS = "static/custom.css"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
