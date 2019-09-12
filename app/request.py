from app import app
from urllib.request,json
import news

News=news.News

api_key=app.config['my_api_key']

base_url=app.config["news_base_url"]

def get_news(category):
    get_news_url=base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        news_results=None
        if get_news_response['sources']:
            
            news_results_list=get_news_response['sources']
            news_results=process_results(news_results_list)
    return news_results
