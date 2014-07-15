#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https:'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing
PLUGINS = ["disqus_static"]

DISQUS_SITENAME = 'geodesygina'
DISQUS_SECRET_KEY = 'jaaoxoW3eIfofTJXNkqJumRS2WSFVXmy7ZmPIpnnc26GeuD49xEhXDv05FltujkC'
DISQUS_PUBLIC_KEY = 'LWuUAL8MsMXypzANGbAiduBOKxey6KrZNFggyvQfhkjHCigVw2tA7hK3Y3xOXuVz'
#GOOGLE_ANALYTICS = ""
