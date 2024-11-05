import os
import sys
from pathlib import Path

# Adicione o caminho do projeto ao sys.path
project_path = Path('/home/lcsmacedo/memorygame')
if project_path not in sys.path:
    sys.path.append(str(project_path))

# Configurações do Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'memorygame.settings'

# Aplicação WSGI do Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
