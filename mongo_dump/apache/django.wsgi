import os
from os import environ
from os.path import dirname, join
from sys import path as PATH
# Installation directory is the parent directory of this file
INSTALL_DIR = dirname(dirname(__file__))
if INSTALL_DIR not in PATH:
    PATH.insert(0, INSTALL_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'restore.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
