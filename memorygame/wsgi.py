import os
import sys
from pathlib import Path

# Adicione o caminho do projeto ao sys.path
path = Path('/home/lcsmacedo/memorygame')
if path not in sys.path:
    sys.path.append(str(path))

# Configurações do Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'memorygame.settings'

# Ativar o ambiente virtual (corrigido)
activate_env = '/home/lcsmacedo/memorygame/venv/bin/activate'
exec(open(activate_env).read(), {'__file__': activate_env})

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
