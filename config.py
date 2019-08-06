import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'k0s0YqDmRpqLb+0TWqbOUouOkSQzZEK+jpFV7onc14Y='
    POSTGRES_USER = 'postgres'
    POSTGRES_PW = 'postgres'
    POSTGRES_URL = '127.0.0.1:5432'
    POSTGRES_DB = 'nubiripple'
    SQLALCHEMY_DATABASE_URI = 'postgres://{user}:{pw}@{url}/{db}'.format(
        user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB)
    # If using RabbitMQ
    CELERY_BROKER_URL = 'amqp://localhost'
    # If using Redis
    # CELERY_BROKER_URL = 'redis://localhost:6379/0'
    # # If using result Backend 
    # CELERY_RESULT_BACKEND = 'postgres://{usuario}:passwprd@{url}/nombre_de_bd'



class ProductionConfig(Config):

    DEBUG = False
    POSTGRES_URL = os.environ.get("POSTGRES_URL")
    POSTGRES_USER = os.environ.get("POSTGRES_USER")
    POSTGRES_PW = os.environ.get("POSTGRES_PW")
    POSTGRES_DB = os.environ.get("POSTGRES_DB")
    SQLALCHEMY_DATABASE_URI = 'postgres://{user}:{pw}@{url}/{db}'.format(
        user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB)
    CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):

    TESTING = True
