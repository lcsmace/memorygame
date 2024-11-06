import os
import sys
from pathlib import Path

# Caminho do projeto
project_path = Path('/home/lcsmacedo/memorygame')
if project_path not in sys.path:
    sys.path.append(str(project_path))

# Configurações do Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'memorygame.settings'

# Ativar o ambiente virtual
activate_env = '/home/lcsmacedo/memorygame/venv/bin/activate'
exec(open(activate_env).read(), {'__file__': activate_env})

# Aplicação WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
