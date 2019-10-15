import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/srv/variable_chef/backend')
sys.path.append('/srv/variable_chef/backend/variable_chef')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'variable_chef.settings')

application = get_wsgi_application()
