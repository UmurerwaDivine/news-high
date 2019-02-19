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
    general_source = get_sources('general')
    business_source = get_sources('business')
    tech_source= get_sources('technology')
    entertainment_source=get_sources('url')
    sport_source = get_sources('sports')

  
    print(general_source)
    
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title=title, general = general_source,technology =tech_source,business=business_source,sports=sport_source,entertainment=entertainment_source)


@app.route('/article/<id>')
def article(id):

    '''
    View root page function that returns the index page and its data
    '''

    # Getting top news
    articles = get_articles(id)
    # title = f'{article.title}'
  
    
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('articles.html', articles=articles)



