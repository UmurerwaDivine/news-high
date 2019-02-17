from flask import render_template
from app import app
from .request import get_sources

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting top news
    top_source = get_sources('top')
    business_source = get_sources('business')
    tech_source = get_sources('techCrunch')
    wall_source = get_sources('wall_street_journal')
    print(top_source)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title,top = top_source,business = business_source,techCrunch = tech_source,wall_street_journal=wall_source)



