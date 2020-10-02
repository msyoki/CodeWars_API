import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://daisy:4H@ppyfeet@localhost/codewars'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    CODEWARS_BASE_URL ='https://www.codewars.com/api/v1/code-challenges/:slug={}?access_key={}'
    CODEWARS_API_KEY= os.environ.key('CODEWARS_API_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):
    '''
    Production configuration child class 
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    '''
    Development configuration child class
    
    Arg:
        config: The parent configuration class with General connfiguration settings
    '''

    DEBUG=True

config_options = {
'development':DevConfig,
'production':ProdConfig
}