from flask import render_template,request,redirect,url_for
# from app import app
from . import main
from ..requests import get_news,get_article

# from .forms import ReviewForm
# from ..models import Review

@main.route('/')
def index():
    title='news_article'
    # general_articles=get_news('technology')
    general=get_news('technology')
    business=get_news('business')
    sports=get_news('sports')

    # sport_articles=get_news('sport')
    return render_template('index.html', title=title,general=general, business=business, sports=sports)
@main.route('/articles/<id>')
def index1(id):
    articles=get_article(id)
    title='news_article'
    return render_template('article.html',title = title,id=id,articles=articles)