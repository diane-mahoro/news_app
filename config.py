import os
class Config:
    '''
    General configuration parent class
    '''
    # pass
    news_base_url='https://newsapi.org/v2/sources?apiKey={}'
    news_api_key=os.environ.get('my_api_key')
    SECRET_KEY=os.environ.get('SECRET_KEY')
    



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