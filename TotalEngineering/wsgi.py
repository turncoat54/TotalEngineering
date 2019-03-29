"""
WSGI config for TotalEngineering project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys

# path = 'C:/code_for_python/TotalEngineering'

# if path not in sys.path:
# 	sys.path.append(path)

from django.core.wsgi import get_wsgi_application



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TotalEngineering.settings")

application = get_wsgi_application()

