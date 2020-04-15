# Fichero de configuracion 
import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "VmLl78572097" 

class ProductionConfig(Config):
    SECRET_KEY = os.environ['SECRET_KEY']
    

class DevelopmentConfig(Config):
    DEBUG = True