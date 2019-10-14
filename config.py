import os

class Config:
    '''
    General configuration parent class
    '''

    NEWS_API_BASE_URL ="https://newsapi.org/v2/sources?apiKey=c1ba4412300d4ff791096a1243b88452"
    ARTICLES_BASE_URL = "https://newsapi.org/v2/top-headlines?country=us&apiKey=c1ba4412300d4ff791096a1243b88452"
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    @staticmethod
    def init_app(app):
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

config_options = {
'development':DevConfig,
'production':ProdConfig
}

