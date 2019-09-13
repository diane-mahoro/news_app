# from app import app
import urllib.request,json
from .models import Sources

# News=models.News
api_key=None
base_url=None
def configure_request(app):
    global api_key,base_url
    api_key = app.config['MY_API_KEY']
    base_url = app.config['news_base_url']
# api_key=app.config['MY_API_KEY']

# base_url=app.config["news_base_url"]

def get_news(category):
    get_news_url=base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        news_results=None
        if get_news_response['sources']:
            
            news_results_list=get_news_response['sources']
            news_results=process_results(news_results_list)
    return news_results

def process_results(news_list):
    '''
    function that process the news results
    '''
    news_results=[]
    for news_item in news_list:
        id=news_item.get('id')
        name=news_item.get('name')
        description=news_item.get('description')
        country=news_item.get('country')
        poster=news_item.get('url')
        if poster:
            news_object=News(id,name,poster,description,country)
            news_results.append(news_object)
    return movie_results




