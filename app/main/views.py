from flask import render_template,request,redirect,url_for
from app import app
from . import main
from ..requests import get_news

# from .forms import ReviewForm
# from ..models import Review

@main.route('/')
def index():
    title='news_article'
    popular_articles=get_news('general')
    return render_template('index.html',title=title, popular=popular_articles)