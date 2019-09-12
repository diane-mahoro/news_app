from flask import render_template
from app import app

@app.route('/')
def index():
    title='news_article'
    return render_template('index.html',title=title)