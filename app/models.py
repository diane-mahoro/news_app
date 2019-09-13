class Sources:
    '''
    News class to define objects
    '''
    def __init__(self,id,name,poster,description,country):
        self.id=id
        self.name=name
        self.poster=poster
        self.description=description
        self.country=country

# class Review:

class Articles:

    def __init__(self,source,author,title,description,url,datepub):
        self.source=source
        self.author=author
        self.title=title
        self.description=description
        self.url=url
        self.datepub=datepub