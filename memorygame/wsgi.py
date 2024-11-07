import sys
import os

# Adicione o caminho do projeto
path = '/home/lcsmacedo/memorygame'
if path not in sys.path:
    sys.path.append(path)

# Defina as configurações do Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'memorygame.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
