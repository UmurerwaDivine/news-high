from flask import render_template,request
from app import app
from .request import get_sources,get_articles
from .models import source,article

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting top news
    # id_source = get_sources('id')
    # name_source = get_sources('name')
    description_source= get_sources('description')
    url_source = get_sources('url')
    # category_source = get_sources('category')
    # language_source = get_sources('language')

    print(description_source)
    print(url_source)
    
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title,description = description_source,url=url_source)
@app.route('/sources/sources<id>')
def articles():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting top news
    # id_article = get_articles('id')
    # name_article = get_articles('name')
    description_article= get_articles('description')
    url_article=get_articles('url')
    # category_article = get_articles('category')
    # language_article = get_articles('language')

    print(url_article)
    print(description_article)
    
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title,description= description_article,url = url_article)




