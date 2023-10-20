from decouple import config

PGSQL_PORT = config('PGSQL_PORT')
PGSQL_HOST = config('PGSQL_HOST')
PGSQL_USER = config('PGSQL_USER')
PGSQL_PASSWORD = config('PGSQL_PASSWORD')
PGSQL_DATABASE = config('PGSQL_DATABASE')

class Config:
    SECRET_KEY = config('SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PGSQL_USER}:{PGSQL_PASSWORD}@{PGSQL_HOST}:{PGSQL_PORT}/{PGSQL_DATABASE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig
}
