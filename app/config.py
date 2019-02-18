class Config:
    '''
    General configuration parent class
    '''
    SOURCE_API_BASE_URL ='https://newsapi.org/v2/sources?apiKey=9a9e8f17ccde48318c9d3274005a1421'
    ARTICLE_API_BASE_URL ='https://newsapi.org/v2/top-headlines?country=us&apiKey=9a9e8f17ccde48318c9d3274005a1421'
    
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