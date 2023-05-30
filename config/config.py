from dotenv import load_dotenv
import os
load_dotenv()

class Config(object):
    """
    This class is used to set the configuration for the application.
    """
    PORT = os.environ.get('PORT') or 3001
    USERNAME = os.environ.get('USERNAME')
    PASSWORD = os.environ.get('PASSWORD')
    DSN = os.environ.get('DSN')
    ENCODING = os.environ.get('ENCODING')
    DEBUG = True
