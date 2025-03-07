import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flavorforge.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
