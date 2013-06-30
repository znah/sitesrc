#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys
sys.path.append('plugins')

AUTHOR = u'Alexander Mordvintsev'
SITENAME = u'Alexander Mordvintsev'
SITEURL = '' # defined in publishconf.py
SITESUBTITLE = u'Teaching computers to see'

TIMEZONE = 'Europe/Paris'

#DELETE_OUTPUT_DIRECTORY = True

DEFAULT_LANG = u'en'

MARKUP = ('rst', 'md', 'html')


THEME = 'themes/notmyidea'

PLUGIN_PATH = 'plugins'
PLUGINS = ['liquid_tags.notebook'] # 'latex'

NOTEBOOK_DIR = '../notebooks'

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'mathjax']

ARTICLE_EXCLUDES = ['pages']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = False
