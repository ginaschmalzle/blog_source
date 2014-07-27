#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Gina Schmalzle'
SITENAME = u'Gina Schmalzle'
SITEURL = 'http://geodesygina.com'

REVERSE_CATEGORY_ORDER = True
TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'
#PLUGIN_PATH = 'plugins'
PLUGINS = ['pelican_youtube']
DISQUS_SITENAME = 'geodesygina'
#DISQUS_SHORTNAME = 'geodesygina'
#DISQUS_SECRET_KEY = 'jaaoxoW3eIfofTJXNkqJumRS2WSFVXmy7ZmPIpnnc26GeuD49xEhXDv05FltujkC'
#DISQUS_PUBLIC_KEY = 'LWuUAL8MsMXypzANGbAiduBOKxey6KrZNFggyvQfhkjHCigVw2tA7hK3Y3xOXuVz'
# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('Hacker School', 'http://hackerschool.com'),
          ('BOS Technologies', 'http://bostechnologies.com'),
	  ('Batu Osmanoglu', 'http://osmanoglu.org/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/GinaSchmalzle'),
          ('Facebook', 'https://www.facebook.com/gschmalzle'),
          ('LinkedIn', 'http://www.linkedin.com/pub/gina-schmalzle/13/8a/234'),
	  ('github', 'https://github.com/ginaschmalzle'),)

DEFAULT_PAGINATION = 10

THEME = '/Users/ginaschmalzle/pelican-themes/blueidea'

STATIC_PATHS = (['images','vectorprojector'])

READERS = {'html': None}

#PAGE_ORDER_BY = 'page-order'

MENUITEMS = [('Home', '/category/home.html'),('Bio', '/category/bio.html'),('Pubs', '/category/pubs.html')]

DISPLAY_PAGES_ON_MENU = False

DISPLAY_CATEGORIES_ON_MENU = False
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
