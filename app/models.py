class Sources:
    '''
    News class to define objects
    '''
    def __init__(self,id,name,url,description,country):
        self.id=id
        self.name=name
        self.url=url
        self.description=description
        self.country=country

class Articles:

    def __init__(self,id,author,urlToImage,publishedAt,description):
        self.id=id
        self.author=author
        self.urlToImage=urlToImage
        self.publishedAt=publishedAt
        self.description=description