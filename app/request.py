import urllib.request, json
from .models import quotes





api_key = None
quotes = None


def configure_request(app):
    global api_key, quotes_url, 
    api_key = app.config['QUOTES_API_KEY']
    quotes_url = app.config['QUOTES_BASE_URL']
    



def process_results(sources_list):
    '''
    Function that processes the json results
    '''
    quotes_results = []

    for quotes in quotes_list:
        id = quotes.get('id')
        description = quotes.get('description')
        url = quotes.get('url')
       

        if url:
            quotes_object = Sources(id,name,description,url)
            quotes_results.append(quotes_object)
    
    return sources_results