# web_project/wsgi.py

"""
WSGI config for web_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_project.settings")

application = get_wsgi_application()

# The following line can be removed if you don't have a separate API application
# app = get_wsgi_application()

# web_project/settings.py
# This line should be in your main settings file, not in the WSGI file
WSGI_APPLICATION = 'web_project.wsgi.application'