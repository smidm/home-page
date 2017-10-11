#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
sys.path.append('.')
from pelicanconf import *

#SITEURL = ''

DELETE_OUTPUT_DIRECTORY = False

FEED_ATOM = None
FEED_RSS = None

# Following items are often useful when publishing

# Uncomment following line for absolute URLs in production:
RELATIVE_URLS = False

DISQUS_SITENAME = "matejsmidcmp"
#GOOGLE_ANALYTICS = ""

STATIC_PATHS = [
    'extra/pages/.htaccess',
    'images',
    'download'
    ]
EXTRA_PATH_METADATA = {
    'extra/pages/.htaccess': {'path': 'pages/.htaccess'},
    }


