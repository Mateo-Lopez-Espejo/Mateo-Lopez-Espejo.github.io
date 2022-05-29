# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
# SITEURL = "http://localhost:8000"
SITEURL = 'https://mateo-lopez-espejo.github.io'
RELATIVE_URLS = False


# update parameters dependent on SITEURL
SITELOGO = SITEURL + '/images/happy_fencer.jpg'
FAVICON = SITEURL + '/images/happy_fencer.jpg'
LINKS = (
    ("CV", SITEURL + "/pdfs/LopezEspejoCV_2022-05-22.pdf"),
)


FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_RSS = 'feeds/{slug}.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""