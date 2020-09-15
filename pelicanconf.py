#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'YOUR NAME'
SITENAME = u'𝒉𝒐𝒏𝒆𝒚𝒑𝒂𝒏𝒄𝒂𝒌𝒆.𝒃𝒌𝒌'
# leave SITEURL blank when developing
SITEURL = ''

PATH = 'content'

# avoid processing .html files
READERS = {'html': None}

# mix articles and static files in the same place
# @see https://github.com/getpelican/pelican/issues/1587
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['articles', 'pages', 'extra', 'images']
EXTRA_PATH_METADATA = {'extra/robots.txt': {'path': 'robots.txt'},
                       'extra/manifest.json': {'path': 'manifest.json'},
                       'extra/pwabuilder-sw.js': {'path': 'pwabuilder-sw.js'},
                       'extra/CNAME': {'path': 'CNAME'},}

# modify TIMEZONE to your timezone
TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = u'th'
LOCALE = 'th_TH.UTF-8'

# @see http://docs.getpelican.com/en/latest/settings.html#basic-settings
# @see http://docs.getpelican.com/en/latest/settings.html#path-metadata
PATH_METADATA = '(articles|pages)/(en|zh|th)/(?P<urlpath>[-a-zA-Z0-9/]*)\.rst'

# @see http://docs.getpelican.com/en/latest/settings.html#url-settings
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_URL = '{urlpath}/'
PAGE_SAVE_AS = '{urlpath}/index.html'

# other possible PATH and URL config
#PATH_METADATA = 'articles[-a-zA-Z0-9/]*/(?P<slug>[-a-zA-Z0-9]*)%(?P<lang>[_a-zA-Z]{2,5})\.rst'
#PATH_METADATA = 'articles/(?P<urlpath>[-a-zA-Z0-9/]*)/(?P<slug>[-a-zA-Z0-9]*)%(?P<lang>[_a-zA-Z]{2,5})\.rst'
#ARTICLE_URL = '{urlpath}/{slug}/'
#ARTICLE_SAVE_AS = '{urlpath}/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# https://github.com/getpelican/pelican/issues/1513
# {tag}tagName syntax not working now
# Update: 3.6.3 looks working now

THEME = 'theme'

PLUGIN_PATHS = ['plugins',
                'plugins/edit_on_github']
PLUGINS = ['i18n_subsites',
           'edit_on_github']

# custom setting for HTML meta info
META_KEYWORDS = 'secondhand clothing, เสื้อผ้ามือสองคุณภาพดี'
META_DESCRIPTION = 'secondhand clothing เสื้อผ้ามือสองคุณภาพดี ราคาน่ารัก🤩 bangkok based styled and modeled by us 💯 have fun shopping!'

# mapping: language_code -> settings_overrides_dict
"""
I18N_SUBSITES = {
  'zh': {
    'SITENAME': '',
    'AUTHOR': '您的姓名',
    'LOCALE': 'zh_TW.UTF-8',
    'META_KEYWORDS': '',
    'META_DESCRIPTION': '',
  },
}
I18N_UNTRANSLATED_ARTICLES = 'remove'
"""

# generate only index.html and pages and articles. (no archives, tags, categories)
#DIRECT_TEMPLATES = ['index']
# use metadata attribute 'order' in page files for ordering
# @see http://docs.getpelican.com/en/latest/settings.html#url-settings
PAGE_ORDER_BY = 'order'

# CONTENT_DIR_URL is the setting for edit_on_github plugin
CONTENT_DIR_URL = u'https://github.com/wangding588/wdpm/tree/master/content'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# custom Jinja2 filter
def hidden_pages_get_page_with_slug_index(hidden_pages):
    for page in hidden_pages:
        if page.slug == "index":
            return page

# custom Jinja2 filter for localizing theme
def gettext(string, lang):
    if lang == "en":
        return string
    elif lang == "zh":
        if string == "Archives": return "歸檔"
        elif string == "Categories": return "分類"
        elif string == "Category": return "分類"
        elif string == "Authors": return "作者"
        elif string == "Author": return "作者"
        elif string == "Tags": return "標籤"
        elif string == "Updated": return "更新"
        elif string == "Translation(s)": return "翻譯"
        elif string == "Edit on Github": return "在Github上編輯"
        else: return string
    elif lang == "th":
        if string == "Archives": return "สารบรรณ"
        elif string == "Categories": return "ประเภท"
        elif string == "Category": return "ประเภท"
        elif string == "Authors": return "ผู้เขียน"
        elif string == "Author": return "ผู้เขียน"
        elif string == "Tags": return "แท็ก"
        elif string == "Updated": return "การปรับปรุง"
        elif string == "Translation(s)": return "การแปล"
        elif string == "Edit on Github": return "แก้ไขที่ Github"
        else: return string
    else:
        return string

JINJA_FILTERS = {
    "hidden_pages_get_page_with_slug_index": hidden_pages_get_page_with_slug_index,
    "gettext": gettext,
}
