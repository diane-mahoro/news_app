from flask import render_template,request,redirect,url_for
# from app import app
from . import main
from ..requests import get_news

# from .forms import ReviewForm
# from ..models import Review

@main.route('/')
def index():
    title='news_article'
    # general_articles=get_news('technology')
    general=get_news('technology')
    business=get_news('business')
    # sport_articles=get_news('sport')
    return render_template('index.html', title=title,general=general, business=business)
