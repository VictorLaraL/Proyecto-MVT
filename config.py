# Fichero de configuracion 
import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "VmLl78572097" 
