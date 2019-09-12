from flask import render_template
from app import app
from .request import get_news

@app.route('/')
def index():
    title='news_article'
    popular_articles=get_news('popular')
    return render_template('index.html',title=title, popular=popular_articles)