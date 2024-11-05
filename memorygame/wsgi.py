import os
import sys
from pathlib import Path

# Adicione o caminho do projeto ao sys.path
project_path = Path('/home/lcsmacedo/memorygame')  # Altere para o caminho correto do seu projeto
if project_path not in sys.path:
    sys.path.append(str(project_path))

# Configurações do Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'memorygame.settings'  # Certifique-se de que este seja o caminho correto para as configurações do Django

# Ativar o ambiente virtual
activate_env = '/home/lcsmacedo/memorygame/venv/bin/activate_this.py'
exec(open(activate_env).read(), {'__file__': activate_env})

# Aplicação WSGI do Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
