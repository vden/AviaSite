# Django settings for avia project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

import os.path
import sys

PROJECT_ROOT = os.path.dirname(__file__)
APPS_ROOT = os.path.join(PROJECT_ROOT, 'src')
sys.path.insert(0, APPS_ROOT)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = os.path.join(PROJECT_ROOT, 'db.sqlite')             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.


APPEND_SLASH=True

DATE_FORMAT = 'd.m.Y'
TIME_FORMAT = 'H:i'

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-ru'

SITE_ID = 1
USE_I18N = True


MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/admin-media/'
PHOTOS_ROOT = os.path.join(MEDIA_ROOT, 'photos')

SECRET_KEY = '!eyi-oy16mx5kpbm-o01g6=o+wi3l9)-82hib%&4vjlq4e@v@s'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',

    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
#    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'core.middleware.PortalMiddleware',

#    'django.middleware.csrf.CsrfResponseMiddleware',
)

ROOT_URLCONF = 'avia.urls'

TEMPLATE_DIRS = (
	os.path.join(PROJECT_ROOT, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.debug",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    "cms.context_processors.media",
)

LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'locale'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'core',
    'news',
    'orders',
    'fts',
    'diagnosis',
	'catalog',

    'tinymce',
    'sorl.thumbnail',

    'cms',
    'publisher',

    'cms.plugins.text',
    'cms.plugins.picture',
    'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.link',
#    'cms.plugins.snippet',
    'cms.plugins.googlemap',
    'cms.plugins.teaser',
    'cms.plugins.video',
#    'cms.plugins.twitter',
    'mptt',
#    'reversion',
)

LANGUAGE_CODE = "ru"

_ = lambda s: s

LANGUAGES = (
    ('ru', _('Russian')),
#    ('es', _('Spain')),
#    ('en', _('English')),
)

CMS_LANGUAGE_CONF = {
    'ru':['en'],
#    'en':['ru'],
#    'es':['es'],
}

CMS_TEMPLATES = (
    ('base.html', _('default')),
)

CMS_SOFTROOT = True
CMS_MODERATOR = False
CMS_PERMISSION = False
CMS_REDIRECTS = True
CMS_SEO_FIELDS = True
CMS_MENU_TITLE_OVERWRITE = True
CMS_HIDE_UNTRANSLATED = True
CMS_FLAT_URLS = False

CMS_TEMPLATE_INHERITANCE = True 

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,paste,searchreplace",
    'theme': "advanced",
'theme_advanced_toolbar_location' : "top",
	'theme_advanced_toolbar_align' : "left",
	'theme_advanced_buttons1' : "search,separator,undo,redo,separator,cut,copy,paste,separator,link,unlink,anchor,separator,tablecontrols,separator,hr",
	'theme_advanced_buttons2' : "styleselect,separator,bold,italic,underline,separator,justifyleft,justifycenter,justifyright,justifyfull,separator,bullist,numlist,outdent,indent,separator,sub,sup,separator,forecolor,backcolor,separator,code",
	'theme_advanced_buttons3' : "",
	'auto_cleanup_word' : 'true',
}

REQUEST_MAIL = "dummy@dummy"
CATALOG_OBJECTS_PER_PAGE = 20

try:
    from settings_local import *
except ImportError:
    pass
