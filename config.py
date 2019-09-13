import os
class Config:
    '''
    General configuration parent class
    '''
    # pass
    NEWS_BASE_URL='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    # MY_API_KEY=os.environ.get('8fd3017f3b8a4a37b60a8b9ff7a58896')
    MY_API_KEY='8fd3017f3b8a4a37b60a8b9ff7a58896'
    SECRET_KEY=os.environ.get('SECRET_KEY')
    pass

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
config_options={
'development':DevConfig,
'production':ProdConfig
}