# from app import app
import urllib.request,json
from .models import Sources,Articles

# News=models.News
api_key=None
base_url=None
article_base_url=None
def configure_request(app):
    global api_key,base_url,article_base_url
    api_key = app.config['MY_API_KEY']
    base_url = app.config['NEWS_BASE_URL']
    article_base_url=app.config['ARTICLES_BASE_URL']

def get_news(category):
    get_news_url=base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        news_results=None
        getNews_data=url.read()
        get_news_response=json.loads(getNews_data)
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
            news_object=Sources(id,name,poster,description,country)
            news_results.append(news_object)
    return news_results
# def get_source(id):
#         get_movie_details
def get_article(id):
    get_article_url=article_base_url.format(id,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        article_results=None
        getArticle_data=url.read()
        get_article_response=json.loads(getArticle_data)
        if get_article_response:
            id=get_article_response.get('id')
            author=get_article_response.get('author')
            urlToImage=get_article_response.get('urlToImage')
            publishedAt=get_article_response.get('publishedAt')
            articles_object=Articles(id,author,urlToImage,publishedAt)
    #         article_results_list=get_article_response['articles']
    #         article_results=process_articles(article_results_list)
        return articles_object

def process_articles(articles_list):
    article_results=[]
    for article_item in article_list:
        id=article_item.get('id')
        author=article_item.get('author')
        urlToImage=article_item.get('urlToImage')
        publishedAt=article_item.get('publishedAt')
        if url:
            articles_object=Articles(id,author,urlToImage,publishedAt)
            article_results.append(articles_object)

    return article_results




