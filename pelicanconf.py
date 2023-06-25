from datetime import datetime

# If your site is available via HTTPS, make sure SITEURL begins with https://
# SITEURL = 'https://mateo-lopez-espejo.github.io'
SITEURL = "http://localhost:8000" # uncomment, run 'pelican -l -r' ,and go to localhost:8000
RELATIVE_URLS = False


AUTHOR = "Mateo López Espejo"
SITENAME = "Mateo López Espejo"
SITETITLE = "Mateo López Espejo"
SITESUBTITLE = " Neuroscience PhD"
SITEDESCRIPTION = "Personal page and blog"
SITELOGO = SITEURL + '/images/happy_fencer.jpg'
FAVICON = SITEURL + '/images/happy_fencer.jpg'
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"

ROBOTS = "index, follow"

# THEME = "/home/mateo/code/Flex"
THEME = "Flex"
PATH = "content/"
OUTPUT_PATH = "output"
TIMEZONE = "America/Vancouver"

DISABLE_URL_HASH = True

# PLUGIN_PATHS = ['pelican-plugins']

# PLUGINS = ['i18n_subsites']

# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "en"
OG_LOCALE = "en_US.utf8"
LOCALE = "en_US.utf8"

DATE_FORMATS = {
    "en": "%Y-%m-%d",
}

# FEED_ALL_ATOM = "feeds/all.atom.xml"
# CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = True

# Avoids a page listing all blog pages, instead uses one blog page as a home page, with no tags
MAIN_MENU = False
HOME_HIDE_TAGS = True

# side panel menu
DISPLAY_PAGES_ON_MENU = True
PAGES_SORT_ATTRIBUTE = "page_order"

LINKS = (
    ("CV", SITEURL + "/pdfs/MateoLopezEspejoCV.pdf"),
)

SOCIAL = (
    ("mastodon", "https://neuromatch.social/@MateoLopezEspejo"),
    ("google", "https://scholar.google.com/citations?user=YR3lRLQAAAAJ&hl=en"),
    ("github", "https://github.com/Mateo-Lopez-Espejo"),
)

# MENUITEMS = (
#     ("Archives", "/archives.html"),
#     ("Categories", "/categories.html"),
#     ("Tags", "/tags.html"),
# )

# CC_LICENSE = {
#     "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
#     "version": "4.0",
#     "slug": "by-sa",
#     "icon": True,
#     "language": "en_US",
# }

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10


STATIC_PATHS = ["images", "pdfs"]


THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True

LOAD_CONTENT_CACHE = True
CACHE_PATH = "cache/"

DELETE_OUTPUT_DIRECTORY = False
