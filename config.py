import os
from sqlalchemy import create_engine
import urllib

class Config(object):
    SECRET_KEY='Clave Unica'
    SESSION_COOKIE_SECURE=False
    
class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://cardiel:root@127.0.0.1/bdhumani'
    SQLALCHEMY_TRACK_MODIFICATIONS=False