from flask import render_template,request,redirect,url_for
# from app import app
from . import main
from ..requests import get_news

# from .forms import ReviewForm
# from ..models import Review

@main.route('/')
def index():
    title='news_article'
    general_articles=get_news('general')
    business_articles=get_news('businesses')
    sport_articles=get_news('sports')
    return render_template('index.html',title=title, general=general_articles, business=business_articles,sport=sport_articles)