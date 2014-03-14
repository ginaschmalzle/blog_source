#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Gina Schmalzle'
SITENAME = u'Gina Schmalzle'
SITEURL = ''

REVERSE_CATEGORY_ORDER = True
TIMEZONE = 'US/New York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('BOS Technologies', 'http://bostechnologies.com'),
          ('Hacker School', 'http://hackerschool.com'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/GinaSchmalzle'),
          ('Facebook', 'https://www.facebook.com/gschmalzle'),
          ('LinkedIn', 'http://www.linkedin.com/pub/gina-schmalzle/13/8a/234'),)

DEFAULT_PAGINATION = 10

THEME = '/Users/ginaschmalzle/pelican-themes/blueidea'

STATIC_PATHS = (['images','vectorprojector'])

READERS = {'html': None}

#PAGE_ORDER_BY = 'page-order'

MENUITEMS = [('Home', '/category/home.html'),('Bio', '/category/bio.html'),('Pubs', '/category/pubs.html')]

DISPLAY_PAGES_ON_MENU = False

DISPLAY_CATEGORIES_ON_MENU = False
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
