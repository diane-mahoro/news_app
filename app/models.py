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

    def __init__(self,source,author,titles,description,url,datepub):
        self.source=source
        self.author=author
        self.titles=titles
        self.description=description
        self.url=url
        self.datepub=datepub