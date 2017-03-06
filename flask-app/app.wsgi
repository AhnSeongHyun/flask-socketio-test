import os, sys
os.environ['PYTHON_EGG_CACHE'] = '/tmp'
from app import create_app
application = create_app()
