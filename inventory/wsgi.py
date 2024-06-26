import os
import sys

# assuming your Django settings file is at
# '/home/myusername/mysite/mysite/settings.py'
path = '/home/shopinventory/shop_inventory'
if path not in sys.path:
     sys.path.insert(0, path)


from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'inventory.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()