"""
WSGI config for inventory project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv
from pathlib import Path

import os
from django.core.wsgi import get_wsgi_application
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory.settings')

application = get_wsgi_application()
