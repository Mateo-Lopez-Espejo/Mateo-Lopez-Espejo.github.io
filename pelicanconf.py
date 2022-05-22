from datetime import datetime

AUTHOR = "Mateo Lopez Espejo"
SITEURL = "http://localhost:8000"
SITENAME = "Mateo Lopez Espejo"
SITETITLE = "Mateo Lopez Espejo"
SITESUBTITLE = " PhD?"
# SITEDESCRIPTION = ""
SITELOGO = 'images/happy_fencer.jpg'
FAVICON = 'images/happy_fencer.jpg'
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"

ROBOTS = "index, follow"

# THEME = "../"
THEME = "/home/mateo/code/Flex"
PATH = "content"
# OUTPUT_PATH = "blog/"
OUTPUT_PATH = "output/"
TIMEZONE = "America/Vancouver"

DISABLE_URL_HASH = True

# PLUGIN_PATHS = ['pelican-plugins']

# PLUGINS = ['i18n_subsites']

# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"

DATE_FORMATS = {
    "en": "%B %d, %Y",
}

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

SOCIAL = (
    ("github", "https://github.com/alexandrevicenzi/Flex"),
    ("rss", "/blog/feeds/all.atom.xml"),
)

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",
    "icon": True,
    "language": "en_US",
}

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 1

DISQUS_SITENAME = "flex-pelican"
ADD_THIS_ID = "ra-55adbb025d4f7e55"

STATIC_PATHS = ["images", "extra/ads.txt", "extra/CNAME"]

EXTRA_PATH_METADATA = {
    "extra/ads.txt": {"path": "ads.txt"},
    "extra/CNAME": {"path": "CNAME"},
}

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True

LOAD_CONTENT_CACHE = False