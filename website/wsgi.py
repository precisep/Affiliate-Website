"""
WSGI config for website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

from affiliate import MyWSGIApp

application = MyWSGIApp()
application = WhiteNoise(application, root='/website/affiliate/Static/affiliate')
application.add_files('/website/affiliate/Static/affiliate', prefix='more-files/')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

application = get_wsgi_application()
