import os

class Config:
    SECRET_KEY ='amir'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOADED_PHOTOS_DEST ='app/static/photos'

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://amir:4567@localhost/myblog'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://amir:4567@localhost/myblog'
    DEBUG = True

class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config:The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
