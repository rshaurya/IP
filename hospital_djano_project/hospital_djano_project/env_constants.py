import os
from dotenv import load_dotenv

load_dotenv('dev.env')

SERVER_HOSTNAME = os.environ.get("SERVER_HOSTNAME", "localhost")
APP_NAME = 'HOSPITAL_DJANO_PROJECT'
REDIRECT_URL = 'https://0.0.0.0:8080/admin'

# Set the env such as DEV, UAT, PROD
ENV = os.environ['ENV']
USE_RDS_LOGGING = os.environ.get("USE_RDS_LOGGING", True)

# constants for database connection configuration
DB_HOSTNAME = os.environ['DB_HOSTNAME']
DB_PORT = os.environ['DB_PORT']
DB_USERNAME = os.environ['DB_USERNAME']

# password must be base64 encoded
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_DBNAME = os.environ['DB_DBNAME']

