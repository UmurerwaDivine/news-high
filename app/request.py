from app import app
import urllib.request,json
from .models import source,article


Source = source.Source
Article = article.Article
# Getting api key
api_key = app.config['NEWS_API_KEY']
base_url = app.config["SOURCE_API_BASE_URL"]
base_url = app.config["ARTICLE_API_BASE_URL"]
def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)


    return source_results
def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        author = source_item.get('author')
        title = source_item.get('title')
        description = source_item.get('description')
        url = source_item.get('url')
        urlToImage = source_item.get('urlToImage')
        publishedAt = source_item.get('publishedAt')
        content = source_item.get('content')

        
        
        # if url:
        source_object = Article(id,name,author,title,description,url,urlToImage,publishedAt,content)
        source_results.append(source_object)


        source_results = None

def get_articles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_results(article_results_list)


    return article_results
def process_results(article_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    article_results = []
    for article_item in article_list:
        id = article_item.get('id')
        name = article_item.get('name')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        
        
        # if url:
        article_object = Article(id,name,author,title,description,url,urlToImage,publishedAt,content)
        article_results.append(article_object)


        article_results = None
   
